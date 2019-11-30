import json
import pandas as pd

with open('data/SP_500.csv') as fp:
	data = pd.read_csv(fp)

db = {}

words_to_ignore = [
	'inc',
	'group',
	'corp',
	'co',
	'plc',
	'ltd'
]

characters_to_ignore = [',', '.']

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

with open('data/tickers.json', 'w+') as fp:
	json.dump(db, fp, indent = 2)