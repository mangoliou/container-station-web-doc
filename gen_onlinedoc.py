# python lib
from __future__ import (
    absolute_import,
    division,
    print_function,
    with_statement
    )
import argparse
import os
import urllib2

# 3rd party lib
from bs4 import BeautifulSoup

site = 'http://qnap.dorowu.com/gitlab/uploads/dorowu/cs-web-auto/'
mask_files = []
rst_files = []


def count_blank(string):
    """Count the Heading blanks."""
    for i, ch in enumerate(string):
        if ch != ' ':
            return i


def mask():
    """Add ignored files to mask."""

    parser = argparse.ArgumentParser(description='Get mask files')
    parser.add_argument('--mask', action="store", dest="mask_files")
    results = parser.parse_args()

    if results.mask_files:
        mask_files.extend(results.mask_files.split(','))

    for f in mask_files:
        if os.path.isfile(f + '.rst'):
            os.remove(f + '.rst')

    # log
    print("Mask Files", mask_files)


def triming_conf():
    """Trim the conf.py."""

    delete_keywords = ['sphinx_rtd_theme', 'sys.path.insert', 'runcode']

    trim_file = []
    with open('conf.py', 'r') as f:
        for line in f:
            for keyword in delete_keywords:
                if keyword in line:
                    break
            else:
                trim_file.append(line)

    with open('conf.py', 'w') as f:
        for line in trim_file:
            f.write(line)


def triming_index():
    """Trim the index.rst file."""

    trim_file = []

    # delete .. exec::
    keep_deleting = False
    with open('index.rst', 'r') as f:
        for line in f:
            if keep_deleting:
                if count_blank(line) > 0 or line.startswith('\n'):
                    pass
                else:
                    trim_file.append(line)
                    keep_deleting = False
            else:
                if '.. exec::' in line:
                    keep_deleting = True
                else:
                    trim_file.append(line)

    # grap all .rst files
    rst_flag = False
    for i, line in enumerate(trim_file):

        if rst_flag:
            if line.startswith('\n') or line.startswith(' '):
                if line != '\n':
                    if line.strip() not in mask_files:
                        rst_files.append(line.strip() + '.rst')
                    else:
                        trim_file[i] = ''
            else:
                rst_flag = False

        if 'maxdepth'in line:
            rst_flag = True

    with open('index.rst', 'w') as f:
        for line in trim_file:
            f.write(line)

    # log
    print("Trimming Files", rst_files)


def gen_dev():
    """
    Generate the 'rtd-requirements.txt' for readthedoc.org's
    advanced setting.
    """

    with open('rtd-requirements.txt', 'w') as f:
        f.write('sphinxcontrib-httpdomain==1.3.0')


def trimming_rest_rst(name):
    """ Trim the ..automodule and ..runcode blocks and parse json response."""

    delete_keywords = ['runcode:: json', 'runcode:: text', 'automodule']
    trim_file = []
    tag = 0

    # trim the file and store to trim_file list
    with open(name, 'r') as f:

        keep_deleting = False
        blank_number = 0
        for line in f:

            if keep_deleting:
                if count_blank(line) > blank_number or line.startswith('\n'):
                    pass
                else:
                    keep_deleting = False
                    blank_number = 0
                    trim_file.append(line)
            else:
                for word in delete_keywords:
                    if word in line:
                        keep_deleting = True
                        if word == 'runcode:: json' or word == 'runcode:: text':
                            trim_file.append(word)
                            blank_number = count_blank(line)
                            tag += 1
                        break
                else:
                    trim_file.append(line)

    # parse_response
    page = urllib2.urlopen(site + name.split('.')[0] + '.html')

    soup = BeautifulSoup(page)
    jsons = soup.findAll('div', attrs={'class': 'highlight-json'})

    texts = soup.findAll('div', attrs={'class': 'highlight-text'})

    # check the number of parsing blocks is same to RUNDOE_TAG
    if tag <= len(jsons) + len(texts):
        print('Blocks is  matching,', name)
        # print('Tag', tag, 'Jsons', len(jsons), 'Text', len(texts))
    else:
        print('Blocks is Not matching,', name)
        print('Tag', tag, 'Jsons', len(jsons), 'Text', len(texts))
        return

    # write result to new file
    with open(name, 'w') as f:

        # replace RUNCODE tag with json and text
        json_block_id = 0
        text_block_id = 0
        for i, line in enumerate(trim_file):

            if line == 'runcode:: json':
                f.write(' '*4 + '.. sourcecode:: json\n\n')
                json = jsons[json_block_id].text.split('\n')
                for l in json:
                    f.write(' '*8 + l + '\n')
                json_block_id += 1
            elif line == 'runcode:: text':
                f.write(' '*4 + '.. sourcecode:: text\n\n')
                text = texts[text_block_id].text.split('\n')
                for l in text:
                    f.write(' '*8 + l + '\n')
                text_block_id += 1
            else:
                f.write(line)


if __name__ == '__main__':

    # mask and delete file
    mask()

    # trim conf.py
    triming_conf()

    # trim index.rst
    triming_index()

    # generate dev files
    gen_dev()

    # trim rest .rst
    for f in rst_files:
        trimming_rest_rst(f)
