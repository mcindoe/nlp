import csv
import json

data = []

file_name = 'full_headlines'

with open('{}.csv'.format(file_name), 'r') as fp:
	reader = csv.reader(fp)

	# skip the first row
	next(reader)

	for row in reader:
		data.append({
			'Headline': row[1],
			'Date': row[2],
			'Provider': row[3]
		})

with open('{}.json'.format(file_name), 'w+') as fp:
	json.dump(data, fp, indent = 2)