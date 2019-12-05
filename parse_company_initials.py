import json

with open('data/word_vectors/SP500_Tickers.json') as fp:
	tickers = json.load(fp)