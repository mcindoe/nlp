import copy
import json
import os

# List of folders containing the JSON files to convert
json_folders = [
	'666_webhose-2015-07_20170904105917',
	'666_webhose-2015-08_20170904105554',
	'666_webhose-2015-09-new_20170904105713',
	'666_webhose-2015-10-new_20170904105820'
]

json_files = []
for folder in json_folders:
	for el in os.listdir(f'WordVectorData/{folder}'):
		json_files.append(f'WordVectorData/{folder}/{el}')

# Undesired punctuation marks
punctuation = ['\n', '.', ',', '"', ':', ';', "'", '(', ')', '%', '$', '@', '£', '+']
numbers = [str(n) for n in range(10)]

# We don't want words containing just these characters:
# (but don't want to remove these characters from other words)
undesirables = numbers + ['-', '/', ' ']

# List to hold every word
text = []

# For each file, get a list of words contained in the text attribute and 
# append to the main list
for file_name in json_files:
	with open(file_name, 'r') as fp:
		file_words = json.load(fp)['text'].split(' ')

	# Remove punctuation
	for i in range(len(file_words)):
		for mark in punctuation:
			while mark in file_words[i]:
				file_words[i] = file_words[i].replace(mark, '')

	# Add words which are not just numbers / remaining punctuation types
	for word in file_words:
		if any(undesirable in word for undesirable in undesirables):
			others = [c for c in word if c not in undesirables]
			if others:
				text.append(f'{word.upper()} ')
		else:
			text.append(f'{word.upper()} ')

	# Add a newline character to separate out article contents
	text.append('\n')

with open('data_dump.txt', 'w+') as fp:
	fp.writelines(text)
