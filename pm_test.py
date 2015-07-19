from urllib import request
import re

url='http://www.stateair.net/web/post/1/5.html'
connection=request.urlopen(url)
html=str(connection.read())    
    
patt=r'Most Recent AQI[\D\d]+\d+ AQI'
matched0=re.findall(patt, html)[0]

patt1=r'\d+ AQI'
matched1=re.findall(patt1, matched0)[0]

patt2=r'\d+'
matched2=float(re.findall(patt2, matched1)[0])

print(matched2)


#'Most Recent AQI[\D\d]+AQI
