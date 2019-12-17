from bs4 import BeautifulSoup
import csv
import os
import re

file_name = '2nd-organisation-of-islamic-cooperation-festival-at-abu-dhabi-national-exhibition-centre-adnec-will-demonstrate-cultural-diversity-and-spread-islamic-messages-of-unity-and-tolerance-to-the-world-804360916.html'
path_to_file = 'scraping/websites/www.prnewswire.com/ae/news-releases/' + file_name

def parse_html(path_to_file, provider):
	try:
		with open(path_to_file, "r") as f:
			contents = f.read()
			soup = BeautifulSoup(contents, 'lxml')

			title = str(soup.title)
			title = title.replace('<title>', '')
			title = title.replace('</title>', '')

			try:
				if provider == 'PR Newswire':
					date = str(soup.findAll(attrs = {"name":"date"})[0])
					date = date[len('<meta content="'): ]
					date = date[:10]

				elif provider in ['Yahoo Finance', 'Express']:
					date = soup.findAll(text = re.compile('datePublished'))[0]
					date_published_index = date.index('datePublished')
					date = date[date_published_index + len('datePublished":') + 1:]
					date = date[:10]

				elif provider == 'Financial News':
					date = soup.findAll(text = re.compile('datetime'))[0]
					datetime_index = date.index('datetime')
					date = date[datetime_index + len('datetime=') + 1:]
					date = date[:10]

				elif provider == 'Money Week':
					date = str(soup.findAll('div', attrs = {"class":"sponsor-entry-meta"}))
					datetime_index = date.index('datetime')
					date = date[datetime_index + len('datetime=') + 1:]
					date = date[:10]

				elif provider == 'UK Investing':
					date = str(soup.findAll('meta', attrs = {"itemprop":"datePublished"}))
					content_index = date.index('content')
					date = date[content_index + len('content=') + 1:]
					date = date[:10]

				elif provider == 'Economic Times India':
					date = soup.findAll(text = re.compile('datePublished'))[0]
					date_published_index = date.index('datePublished')
					date = date[date_published_index + len('datePublished":') + 2:]
					date = date[:10]

				elif provider in ['BWM Online', 'Fast Company', 'The Independent']:
					date = str(soup.findAll(
						'meta', 
						attrs = {"property": "article:published_time"}
					)[0])
					content_index = date.index('content')

					date = date[content_index + len('content=') + 1:]
					date = date[:10]

			except:
				file_name = path_to_file.split('/')[-1]
				print(f'Could not find a date, {file_name}')
				return False

			return title, date
	
	except:
		return False


# if __name__ == '__main__':
# 	test = parse_html(
# 		'/Volumes/My Passport for Mac/scrapes/websites/fortune.com/100-fastest-growing-companies/2014/ensco-81/index.html',
# 		'Fortune'
# 	)
# 	print(test)

