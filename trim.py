# python lib
from __future__ import absolute_import, division, print_function, with_statement
import urllib2

# 3rd party lib
from bs4 import BeautifulSoup

site = 'http://qnap.dorowu.com/gitlab/uploads/dorowu/cs-web-auto/'
rst_files = [
	'system.rst',
    'container.rst',
    'create.rst',
    'compose.rst',
    'resource.rst',
    'image.rst',
    'import.rst',
    'backup.rst',
    'log.rst',
    'preference.rst',
    'draft.rst',
]

def count_starting_blank(string):
	
	for i, ch in enumerate(string):
		if ch != ' ':
			return i 

def trimming(name):

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
				if count_starting_blank(line) > blank_number or line.startswith('\n'):
					pass
				else:
					keep_deleting = False
					blank_number = 0
					trim_file.append(line)
			else:
				for word in delete_keywords:
					if word in line:
						keep_deleting = True
						if word=='runcode:: json' or word=='runcode:: text':
							trim_file.append(word)
							blank_number = count_starting_blank(line)
							tag += 1
						break
				else:
					trim_file.append(line)

	# parse_response
	page = urllib2.urlopen(site + name.split('.')[0] + '.html')

	soup = BeautifulSoup(page)
	jsons = soup.findAll('div', attrs={'class' : 'highlight-json'})

	texts = soup.findAll('div', attrs={'class' : 'highlight-text'})

	# check the number of parsing blocks is same to RUNDOE_TAG
	if tag <= len(jsons) + len(texts):
		print('Blocks is  matching,', name)
		#print('Tag', tag, 'Jsons', len(jsons), 'Text', len(texts))
	else:
		print('Blocks is Not matching,', name)
		print('Tag', tag, 'Jsons', len(jsons), 'Text', len(texts))
		return


	# write result to new file
	with open('_' + name, 'w') as f:
		
		# replace RUNCODE tag with json 
		json_block_id = 0
		text_block_id = 0
		for i, line in enumerate(trim_file):

			if line=='runcode:: json':
				f.write(' '*4 + '.. sourcecode:: json\n\n')
				json = jsons[json_block_id].text.split('\n')  
				for l in json:
					f.write(' '*8 + l + '\n')
				json_block_id += 1
			elif line=='runcode:: text':
				f.write(' '*4 + '.. sourcecode:: text\n\n')
				text = texts[text_block_id].text.split('\n')  
				for l in text:
					f.write(' '*8 + l + '\n')
				text_block_id += 1				
			else:
				f.write(line)


if __name__ == '__main__':

	for f in rst_files:
		trimming(f)
	#trimming('import.rst')