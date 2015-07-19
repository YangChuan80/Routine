import re
import urllib.request

url='http://www.khou.com/weather/'

connection=urllib.request.urlopen(url)

html=str(connection.read())

patt=r'Houston, TX\D+"degree">\d+\D+outlook\D+</span></a></li><li'
matched=re.findall(patt, html)[0]

degree=float(re.findall(r'\d+', matched)[0])

print(degree)

outlook=re.findall(r'outlook\D+', matched)[0]
outlook=outlook.replace(r'outlook">','').replace(r'</span></a></li><li', '')

print(outlook)


