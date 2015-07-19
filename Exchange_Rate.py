import re
from urllib import request

url=r'http://www.bloomberg.com/quote/USDcny:CUR'

connection=request.urlopen(url)
html_raw=connection.read()
html=str(html_raw)

patt=r'USD-CNY\D+\d+.\d+\D+Price of 1 USD in CNY'

matched_raw=re.findall(patt, html)[0]

digit_patt=r'\d+.\d+'
matched=float(re.findall(digit_patt, matched_raw)[0])

print(matched)
