import csv
import json
import pandas as pd

# Read in data table
with open('data/SP_500.csv') as fp:
	data = pd.read_csv(fp)

# List of common company words to ignore, following along with the paper's methodology
words_to_ignore = [
	'inc',
	'group',
	'corp',
	'co',
	'plc',
	'ltd'
]

# Characters to ignore in the company names
characters_to_ignore = [',', '.']

# Create Database
db = {}
for index, row in data.iterrows():
	# Ignore the last two rows which contain information about the table
	if index < len(data) - 2:
		name = row['Name'].lower()
		for c in characters_to_ignore:
			while c in name:
				name = name.replace(c, '')

		words = [x for x in name.split(' ') if x not in words_to_ignore]
		name = ' '.join(words)

		db[name.upper()] = row['Ticker']

# Write Database to JSON format
with open('data/SP500_Tickers.json', 'w+') as fp:
	json.dump(db, fp, indent = 2)

# Write Database to CSV format
with open('data/SP500_Tickers.csv', 'w+') as fp:
	writer = csv.writer(fp)
	headers = ['Name', 'Ticker']

	writer.writerow(headers)
	for key, val in db.items():
		writer.writerow([key, val])