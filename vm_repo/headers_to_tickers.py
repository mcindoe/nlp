import json
import nltk
from nltk.tag import StanfordNERTagger
import os
import spacy
import textacy

def get_ticker(name, tickers, max_words):
	'''Replace one (possible multiple-word) organisation name with its ticker
	
	Params:
	name (str): Company name (possibly multiple words)
	tickers (dict): Dictionary of (name, ticker) pairs
	max_words (number): The maximum number of words of any company name in tickers
	'''

	# Get the list of the words in the company name
	company_words = name.split(' ')

	for word_count in reversed(range(1, min(max_words, len(company_words))+1)):
		for index in range(0, len(company_words) - word_count + 1):
			subset = ' '.join(company_words[index : index+word_count])
			for company, ticker in tickers.items():
				# If this phrase is a substring of a company name, return that 
				if subset.lower() in company.lower():
					return ticker

				# If this is already a ticker, return that
				if subset.lower() == ticker.lower():
					return ticker

	return None

def parse_header(header, max_company_name_length):
	'''Attempt to replace all organisations in a header with their ticker'''
	tokens = nltk.word_tokenize(header)
	
	try:
		classified_text = st.tag(tokens)
		print('classified_text', classified_text)
	except OSError:
		print('OS Error, likely could not allocate memory')
		return

	parsed_words = []

	# If multiple words in a row are organisations, we want to group
	# these together and check if they are tickers
	i = 0
	while i < len(classified_text):
		if classified_text[i][1] in COMPANY_TYPES:
			# Get the list of consecutive words until the next word is not
			# of type 'ORGANIZATION'
			words_to_classify = [classified_text[i][0]]
			index = 1
			while True:
				# print(i + index)
				# print(classified_text[i + index])

				if i + index >= len(classified_text):
					break
				if classified_text[i + index][1] not in COMPANY_TYPES:
					break
				
				words_to_classify.append(classified_text[i + index][0])
				index += 1

			complete_organisation = [' '.join(words_to_classify), 'ORGANIZATION']
			parsed_words.append(complete_organisation)
			i += index

		else:
			parsed_words.append(list(classified_text[i]))
			i += 1

	for i in range(len(parsed_words)):
		word, classification = tuple(parsed_words[i])

		if classification == 'ORGANIZATION':
			ticker = get_ticker(word, tickers, max_company_name_length)
			if ticker is not None:
				parsed_words[i][0] = f'__{ticker}'

	return ' '.join(x[0] for x in parsed_words)

if __name__ == '__main__':
	COMPANY_TYPES = ['PERSON', 'ORGANIZATION']
	JAVA_PATH = '/usr/lib/jvm/java-8-openjdk-amd64'
	os.environ['JAVAHOME'] = JAVA_PATH

	# Load dictionary of (company:ticker) values
	with open('tickers.json', 'r') as fp:
		tickers = json.load(fp)

	max_company_name_length = max((len(x) for x in tickers))

	# Load list of dictionaries of (header, date, provider)
	with open('main.json', 'r') as fp:
		data = json.load(fp)

	# Limit headers for testing
	data = data[:5]
	print('LIMITING DATA')

	# Load "en_core_web_sm" NLP. To download, first pip install spacy, then 
	# enter in a terminal "python3 -m spacy download en_core_web_sm"
	nlp = spacy.load('en_core_web_sm')

	st = StanfordNERTagger(
	    'stanford-ner-2014-06-16/classifiers/english.all.3class.distsim.crf.ser.gz',
	    'stanford-ner-2014-06-16/stanford-ner.jar',
	    encoding = 'utf-8'
	)

	nlp = spacy.load('en_core_web_sm')

	for el in data:
		header = el['Headline']
		test = parse_header(header, max_company_name_length)
		print(test)

		# extraction = list(textacy.extract.subject_verb_object_triples(nlp(header)))
		# print('extraction', extraction)