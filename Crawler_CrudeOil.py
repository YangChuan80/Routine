import re
from urllib import request

url='http://www.bloomberg.com/energy/'
connection=request.urlopen(url)

html_byte=connection.read()
html=str(html_byte)

brent=r'Brent\D+\d+.\d+'
wti=r'WTI\D+\d+.\d+'


brent_str=str(re.findall(brent, html))

wti_str=str(re.findall(wti, html))

index=r'\d+.\d+'

brent_index=float(re.findall(index, brent_str)[0])
wti_index=float(re.findall(index, wti_str)[0])

print('Realtime Crude Oil Price:')
print('Brent Index: ', brent_index)
print('WTI Index: ', wti_index)