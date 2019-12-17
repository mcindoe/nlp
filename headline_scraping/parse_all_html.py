import glob
from itertools import chain
import json
import os

from parse_html import parse_html

providers = {
	# 'Economic Times India': 'economictimes.indiatimes.com',
	# 'Yahoo Finance': 'uk.finance.yahoo.com',
	# 'Financial News': 'financial-news.co.uk',
	# 'UK Investing': 'uk.investing.com',
	# 'PR Newswire': 'www.prnewswire.com',
	# 'Money Week': 'www.moneyweek.com',
	# 'BWM Online': 'www.bwmonline.com',
	# 'Fast Company': 'www.fastcompany.com',
	'The Independent': 'www.independent.co.uk'
}

root = '/Volumes/My Passport for Mac/scrapes/websites/'

for provider, provider_folder in providers.items():

	print('provider', provider)

	data = []

	if provider == 'Economic Times India':
		file_type = 'cms'
	else:
		file_type = 'html'

	files = glob.iglob(root + '/' + provider_folder + f'/**/*.{file_type}', recursive = True)

	print('Starting process')
	for file in files:
		try:
			output = parse_html(file, provider)
			if output:
				title, date = output
				data.append([title, date, provider])

		except:
			pass

	with open(f'parsed_scrapes/{provider}.json', 'w+') as fp:
		json.dump(data, fp, indent = 2)