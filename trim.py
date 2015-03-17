# python lib
from __future__ import absolute_import, division, print_function, with_statement
import urllib2

# 3rd party lib
from bs4 import BeautifulSoup

site = 'http://qnap.dorowu.com/gitlab/uploads/dorowu/cs-web-auto/'
rst_files = ['system.rst']


def trimming(name):

	""" Trim the ..automodule and ..runcode blocks and parse json response."""

	delete_keywords = ['runcode', 'automodule']
	trim_file = []
	runcode_num = 0

	# trim the file and store to trim_file list
	with open(name, 'r') as f:

		keep_deleting = False
		for line in f:
			
			if keep_deleting:
				if line.startswith(' ') or line.startswith('\n') or line.startswith('\t'):
					pass
				else:
					keep_deleting = False
					trim_file.append(line)
			else:
				for word in delete_keywords:
					if word in line:
						keep_deleting = True
						if word=='runcode':
							trim_file.append('RUNCODE')
							runcode_num += 1
						break
				else:
					trim_file.append(line)

	# parse_response_json
	page = urllib2.urlopen(site + name.split('.')[0] + '.html')

	soup = BeautifulSoup(page)
	jsons = soup.findAll('div', attrs={'class' : 'highlight-json'})

	if runcode_num != len(jsons):
		print('Blocks is not matching', name)
		return
	else:
		print('Blocks is matching', name)
	


	# write result to new file
	with open('_' + name, 'w') as f:
		
		# replace RUNCODE tag with json 
		block_id = 0
		for i, line in enumerate(trim_file):

			if line=='RUNCODE':
				
				f.write(' '*4 + '.. sourcecode:: json\n\n')
				json = jsons[block_id].text.split('\n')  
				for l in json:
					f.write(' '*8 + l + '\n')
				block_id += 1

			else:
				f.write(line)

if __name__ == '__main__':

	trimming('system.rst')
"""
	page = urllib2.urlopen('http://qnap.dorowu.com/gitlab/uploads/dorowu/cs-web-auto/system.html')

	soup = BeautifulSoup(page)
	texts = soup.findAll('div', attrs={'class' : 'highlight-json'})
	print(len(texts))
	#for t in texts:
	#	print(t.text)
"""
"""
	delete_keywords = ['runcode', 'automodule']
	trim_file = []


	with open('system.rst', 'r') as f:

		keep_deleting = False
		for line in f:
			
			if keep_deleting:
				if line.startswith(' ') or line.startswith('\n') or line.startswith('\t'):
					pass
				else:
					keep_deleting = False
					trim_file.append(line)
			else:
				for word in delete_keywords:
					if word in line:
						keep_deleting = True
						break
				else:
					trim_file.append(line)

	with open('_system.rst', 'w') as f:
		for line in trim_file:
			f.write(line);
"""
