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

# Split into two lists
list_1_length = int(len(json_files) / 2)

file_sublists = {
	'list1': json_files[:list_1_length],
	'list2': json_files[list_1_length:]
}

# Undesired punctuation marks
punctuation = ['\n', '.', ',', '"', ':', ';', "'", '(', ')', '%', '$', '@', '£', '+']
numbers = [str(n) for n in range(10)]

# We don't want words containing just these characters:
# (but don't want to remove these characters from other words)
undesirables = numbers + ['-', '/', ' ']

# List to hold every word
text_lists = {name: [] for name in file_sublists}

# For each file, get a list of words contained in the text attribute and 
# append to the main list
for name in file_sublists:
	for file_name in file_sublists[name]:
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
					file_sublists[name].append(f'{word.upper()} ')
			else:
				file_sublists[name].append(f'{word.upper()} ')

		# Add a newline character to separate out article contents
		file_sublists[name].append('\n')

for i, name in enumerate(file_sublists):
	with open(f'data_dump_{i}.txt', 'w+') as fp:
		fp.writelines(file_sublists[name])
