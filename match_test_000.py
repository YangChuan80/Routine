from urllib import request
import re

url='http://www.khou.com/weather/'
connection=request.urlopen(url)

html=str(connection.read())
#patt=r'Houston, TX\D+"degree">\d+\D+outlook\D+</span></a></li><li'
weather_pattern=r'current-temp">\d+\D+\d+\D+"outlook">[\w.]+</p>'
matched=re.findall(weather_pattern, html)[0]

degree=float(re.findall(r'\d+', matched)[0])
feel_like=float(re.findall(r'\d+', matched)[1])

outlook=re.findall(r'outlook">\D+', matched)[0]
outlook=outlook.replace(r'outlook">','').replace(r'</p>', '')

connection.close()
