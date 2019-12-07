import pandas as pd

data = pd.read_csv('main.csv')

data = data[pd.to_datetime(data['Date'], format='%Y-%m-%d', errors='coerce').notnull()]
data.to_csv('main.csv')