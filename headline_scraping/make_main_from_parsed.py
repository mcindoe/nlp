import csv
import json

providers = [
	'Economic Times India',
	'Yahoo Finance',
	'Financial News',
	'UK Investing',
	'PR Newswire',
	'Money Week',
	'BWM Online',
	'Fast Company',
	'The Independent',
]

# Write headers row
with open('full_headlines.csv', 'w+') as fp:
	writer = csv.writer(fp)
	writer.writerow(['Headline', 'Date', 'Provider'])

# Write each provider's contents to the CSV
for provider in providers:
	with open('{}.json'.format(provider), 'r') as fp:
		data = json.load(fp)

	with open('full_headlines.csv', 'a') as fp:
		writer = csv.writer(fp)

		for row in data:
			writer.writerow(row)