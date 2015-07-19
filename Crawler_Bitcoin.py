import re
from urllib import request

url='https://www.coinbase.com/charts'

connection=request.urlopen(url)
html=str(connection.read())

bitcoin_pattern=r'BTC = \$\d+.\d+'
matched=re.findall(bitcoin_pattern, html)[0]

price=float(re.findall(r'\d+.\d+', matched)[0])

print(price)

