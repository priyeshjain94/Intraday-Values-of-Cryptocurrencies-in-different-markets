# Source(s):  
# [http://www.alphavantage.co/documentation]

from alpha_vantage.cryptocurrencies import CryptoCurrencies
from pprint import pprint


Cryp = CryptoCurrencies(key='YOUR_API_KEY', output_format = 'pandas')
Data, meta_data = Cryp.get_digital_currency_intraday(symbol='BTC', market='INR')

pprint(Data.head(2))

#head(2) represents 2 entries of different intervals

import matplotlib.pyplot as plt

plt.figure(figsize=(10,10))

Data['1a. price (INR)'].plot()

plt.tight_layout()

plt.title('Intraday value for bitcoin (BTC)')

plt.grid()

#plt.show()

plt.savefig('CurrencyPlot.png')

'''
#JSON Format
''
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from pprint import pprint

import json

import requests
r = requests.get('https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_INTRADAY&symbol=BTC&market=INR&apikey=YOUR_API_KEY')
print r.json()

Cryp = CryptoCurrencies(key='YOUR_API_KEY', output_format = 'pandas')

Data, meta_data = Cryp.get_digital_currency_intraday(symbol='BTC', market='INR')

pprint(r)

pprint(Data.head(2))

#head(number) signifies the number of results one wants to see

import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))

Data['1a. price (INR)'].plot()
plt.tight_layout()
plt.title('Intraday value for bitcoin (BTC)')
plt.show()
''
'''
