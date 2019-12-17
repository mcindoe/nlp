import csv
import json

providers = [
	'Economic Times India',
	'Financial News',
	'UK Investing'
]

with open('main.csv', 'w+') as fp:
	writer = csv.writer(fp)
	writer.writerow(['Headline', 'Date', 'Provider'])

for provider in providers:
	with open('{}.json'.format(provider), 'r') as fp:
		data = json.load(fp)

	with open('main.csv', 'a') as fp:
		writer = csv.writer(fp)

		for row in data:
			writer.writerow(row)