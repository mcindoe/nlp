'''
Gets the header of every article in the data/word_vectors/raw folders
'''
import csv
import json
import os
import unicodedata

# List of folders containing the JSON files to convert
json_folders = [
	'666_webhose-2015-07_20170904105917',
	'666_webhose-2015-08_20170904105554',
	'666_webhose-2015-09-new_20170904105713',
	'666_webhose-2015-10-new_20170904105820'
]

# Get a list of the relative paths of all of the JSON files
folder_path = 'data/word_vectors/raw'
json_files = []
for folder in json_folders:
	for el in os.listdir(f'{folder_path}/{folder}'):
		json_files.append(f'{folder_path}/{folder}/{el}')

# Extract the header from each JSON file
headers = []
for file in json_files:
	with open(file, 'r') as f:
		data = json.load(f)
		header = data['title']
		date = data['published'][:9]
		headers.append({
			'header': header,
			'date': date
		})

# Create a dictionary to write to file
output = {'headers': headers}

# Write the list to file
with open('data/word_vectors/article_headers_with_dates.json', 'w+') as file:
	# Disabling ensure_ascii - allows e.g. quote marks and $ signs to appear
	# I think this is the approach we want
	writer = csv.writer(file)
	writer.writerow(['Date', 'Header'])
	for el in output['headers']:
		print(el)
		writer.writerow([el['date'], el['header']])