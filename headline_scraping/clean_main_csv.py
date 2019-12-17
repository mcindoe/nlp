'''
Check each row for a valid date string, by attempting to parse it as a
datetime object. If not valid, exclude the row
'''

import pandas as pd

data = pd.read_csv('main.csv')

valid_rows = pd.to_datetime(
	data['Date'], 
	format = '%Y-%m-%d', 
	errors = 'coerce'
).notnull()

data[valid_rows].to_csv('main.csv')