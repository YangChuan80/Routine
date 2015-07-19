from urllib import request
import re
import datetime

def crude_oil_detect():
    url='http://www.bloomberg.com/energy/'
    connection=request.urlopen(url)
    html_byte=connection.read()
    html=str(html_byte)

    brent_regrex=r'Brent\D+\d+.\d+'
    wti_regrex=r'WTI\D+\d+.\d+'
    brent_str=str(re.findall(brent_regrex, html))
    wti_str=str(re.findall(wti_regrex, html))

    uni_regrex=r'\d+.\d+'
    brent_index=float(re.findall(uni_regrex, brent_str)[0])
    wti_index=float(re.findall(uni_regrex, wti_str)[0])
    
    connection.close()
    
    return brent_index, wti_index

def exchange_rate_detect():
    url=r'http://www.bloomberg.com/quote/USDcny:CUR'
    connection=request.urlopen(url)
    html_raw=connection.read()
    html=str(html_raw)

    exchange_regex=r'USD-CNY\D+\d+.\d+\D+Price of 1 USD in CNY'

    matched_raw=re.findall(exchange_regex, html)[0]
    digit_patt=r'\d+.\d+'
    rate=float(re.findall(digit_patt, matched_raw)[0])
    
    connection.close()

    return rate
    
def bitcoin_price_detect():
    url='https://www.coinbase.com/charts'
    connection=request.urlopen(url)
    html=str(connection.read())

    bitcoin_pattern=r'BTC = \$\d+.\d+'
    matched=re.findall(bitcoin_pattern, html)[0]
    price=float(re.findall(r'\d+.\d+', matched)[0])
    
    connection.close()

    return price
    
def weather_detect():
    url='http://www.khou.com/weather/'
    connection=request.urlopen(url)

    html=str(connection.read())
    patt=r'Houston, TX\D+"degree">\d+\D+outlook\D+</span></a></li><li'
    matched=re.findall(patt, html)[0]

    degree=float(re.findall(r'\d+', matched)[0])
    outlook=re.findall(r'outlook\D+', matched)[0]
    outlook=outlook.replace(r'outlook">','').replace(r'</span></a></li><li', '')
    outlook=outlook.title()
    
    connection.close()

    return degree, outlook  
    
def gold_price_detect():
    url='http://www.jmbullion.com/charts/gold-price/'
    connection=request.urlopen(url)
    html=str(connection.read())    
    
    gold_regrex=r'gounce\D+\d+,\d+.\d+'
    matched=re.findall(gold_regrex, html)[0]
    gold=float(re.findall(r'\d+,\d+.\d+', matched)[0].replace(',', ''))
    
    connection.close()
    
    return gold
    
def pm_detect():
    url='http://www.stateair.net/web/post/1/5.html'
    connection=request.urlopen(url)
    html=str(connection.read())    
        
    patt=r'Most Recent AQI[\D\d]+\d+ AQI'
    matched0=re.findall(patt, html)[0]

    patt1=r'\d+ AQI'
    matched1=re.findall(patt1, matched0)[0]

    patt2=r'\d+'
    matched2=re.findall(patt2, matched1)[0]
    
    pm=float(matched2)
    
    return pm

def refresh():
    brent, wti=crude_oil_detect()
    exchange=exchange_rate_detect()
    bitcoin=bitcoin_price_detect()
    degree, outlook=weather_detect()
    gold=gold_price_detect()
    pm=pm_detect()
    
    t=datetime.datetime.now()
    
    print('Realtime Indeces')
    print('Current Time: ', t, '\n')
    
    print('Weather of Houston:')
    print('Temperature: %s°F, Outlook: %s\n'%(degree, outlook))
    
    print('US DOLLAR-CHINA RENMINBI Exchange Rate')
    print('USD-CNY: RMB￥%s/Dollar\n'%exchange)
    
    print('Air Quality Monitor - The U.S. Consulate in Shenyang')
    print('PM2.5: %s\n'%pm)
    
    print('Crude Oil Price:')
    print('Brent Index: $%s/bbl.'%brent)
    print('WTI Index: $%s/bbl.\n'%wti)   
    
    print('Gold Price:')
    print(' $%s/ounce.\n'%gold)   
    
    print('Bitcoin Price:')
    print(' $%s/Bitcoin\n'%bitcoin)   
    
if __name__=='__main__':
   refresh()