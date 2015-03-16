from __future__ import absolute_import, division, print_function, with_statement


if __name__ == '__main__':

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

