from urllib import request
import re
import datetime
import tkinter
import time

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
    weather_pattern=r'Houston, TX\D+"degree">\d+\D+outlook">\D+</span></a></li><li'
    matched=re.findall(weather_pattern, html)[0]

    degree=float(re.findall(r'\d+', matched)[0])
        
    outlook=re.findall(r'outlook">\D+', matched)[0]
    outlook=outlook.replace(r'outlook">','').replace(r'</span></a></li><li', '')
    outlook=outlook.title()
    
    connection.close()

    return degree, outlook  
    
def gold_price_detect():
    url='http://www.jmbullion.com/charts/gold-price/'
    connection=request.urlopen(url)
    html=str(connection.read())    
    
    gold_pattern=r'gounce\D+\d+,\d+.\d+'
    matched=re.findall(gold_pattern, html)[0]
    gold=float(re.findall(r'\d+,\d+.\d+', matched)[0].replace(',', ''))
    
    connection.close()
    
    return gold
    
def pm_detect():
    url='http://www.stateair.net/web/post/1/5.html'
    connection=request.urlopen(url)
    html=str(connection.read())    
        
    pm_pattern=r'Most Recent AQI[\D\d]+\d+ AQI'
    matched0=re.findall(pm_pattern, html)[0]

    patt1=r'\d+ AQI'
    matched1=re.findall(patt1, matched0)[0]

    patt2=r'\d+'
    matched2=re.findall(patt2, matched1)[0]
    
    pm=float(matched2)
    
    return pm

def get():
    global brent, wti, exchange, bitcoin, degree, outlook, gold, pm, level, t
    
    error='ErrorConnection!'
    
    try:
        brent, wti=crude_oil_detect()
    except Exception:
        brent, wti=error, error
        
    try:
        exchange=exchange_rate_detect()
    except Exception:
        exchange=error
        
    try:
        bitcoin=bitcoin_price_detect()
    except Exception:
        bitcoin=error
    
    try:
        degree, outlook=weather_detect()
    except Exception:
        degree, outlook=error, error
    
    try:
        gold=gold_price_detect()
    except Exception:
        gold=error
        
    try:
        pm=pm_detect()
    except Exception:
        pm=error    
    
    if pm<=50:
        level='Good'

    elif pm>50 and pm<=100:
        level='Moderate'

    elif pm>100 and pm<=150:
        level='Unhealthy for Sensitive Groups'

    elif pm>150 and pm<=200:
        level='Unhealthy'

    elif pm>200 and pm<=300:
        level='Very Unhealthy'

    elif pm>300 and pm<=500:
        level='Hazardous'

    elif pm>500:
        level='Beyond Index' 
    else:
        pm=error
    
    t=datetime.datetime.now()

#///////Main/////////////////////////////////////////////////////////////////////////////
if __name__=='__main__': 
   
    #////Window Establishment//////////////////////////////////////
    root=tkinter.Tk()
    
    root.geometry('730x680+80+20')
    root.title('Spider -- A Realtime Index Tool')
    
    #//////Label//////////////////////////////////////////////////
    #Title Label    
    label_title=tkinter.Label(root,text='Realtime Indeces', font=30)
    label_title.place(x=280,y=10)
    
    #Datetime Label    
    label_datetime=tkinter.Label(root,text='Current Datetime: ', font=30)
    label_datetime.place(x=180,y=50)
    
    #Weather Label    
    label_weather=tkinter.Label(root,text='Weather of Houston, TX: ', font=30)
    label_weather.place(x=180,y=110)
    
    #Temperature Label    
    label_degree=tkinter.Label(root,text='Temperature: ', font=30)
    label_degree.place(x=50,y=150)
    
    #Fahrenheit Label    
    label_fahrenheit=tkinter.Label(root,text='°F', font=30)
    label_fahrenheit.place(x=270,y=150)
    
    #Exchange Label    
    label_exchange=tkinter.Label(root,text='US DOLLAR-CHINA RENMINBI Exchange Rate:', font=30)
    label_exchange.place(x=180,y=210)
    
    #RMB Label    
    label_rmb=tkinter.Label(root,text='USD-CNY: RMB￥', font=30)
    label_rmb.place(x=50,y=250)
    
    #PerDollar Label    
    label_rmb=tkinter.Label(root,text='/Dollar', font=30)
    label_rmb.place(x=280,y=250)
    
    #Crude Oil Price Label    
    label_crude=tkinter.Label(root,text='Crude Oil Price:', font=30)
    label_crude.place(x=180,y=310)

    #$ Label    
    label_dollar0=tkinter.Label(root,text='Brent Index: $', font=30)
    label_dollar0.place(x=50,y=350)

    #$ Label    
    label_dollar1=tkinter.Label(root,text='WTI Index: $', font=30)
    label_dollar1.place(x=370,y=350)

    #PerBarrel Label    
    label_perbarrel0=tkinter.Label(root,text='/bbl.', font=30)
    label_perbarrel0.place(x=270,y=350)

    #PerBarrel Label    
    label_perbarrel1=tkinter.Label(root,text='/bbl.', font=30)
    label_perbarrel1.place(x=572,y=350)

    #Gold Price Label    
    label_gold=tkinter.Label(root,text='Gold Price:', font=30)
    label_gold.place(x=80,y=410)

    #$ Label    
    label_dollar2=tkinter.Label(root,text='$', font=30)
    label_dollar2.place(x=50,y=450)

    #PerOunce Label    
    label_ounce=tkinter.Label(root,text='/ounce.', font=30)
    label_ounce.place(x=215,y=450)

    #Bitcoin Price Label    
    label_bitcoin=tkinter.Label(root,text='Bitcoin Price:', font=30)
    label_bitcoin.place(x=480,y=410)

    #$ Label    
    label_dollar3=tkinter.Label(root,text='$', font=30)
    label_dollar3.place(x=450,y=450)

    #PerBitcoin Label    
    label_perbitcoin=tkinter.Label(root,text='/Bitcoin', font=30)
    label_perbitcoin.place(x=572,y=450)
    
    #PM 2.5 Title Label    
    label_pm_title=tkinter.Label(root,text='Air Quality Monitor - The U.S. Consulate in Shenyang', font=30)
    label_pm_title.place(x=120,y=510)

    #PM 2.5 Label    
    label_pm=tkinter.Label(root,text='PM2.5:', font=30)
    label_pm.place(x=110,y=550)

    #AQI Label    
    label_aqi=tkinter.Label(root,text='AQI', font=30)
    label_aqi.place(x=273,y=550)
    
    #//////Text/////////////////////////////////////////////////////
    #Datetime Text
    text_datetime=tkinter.Text(root,width=32,height=1, font=20)
    text_datetime.place(x=330,y=50)   
    text_datetime.delete('1.0', tkinter.END)
    
    #Degree Text
    text_degree=tkinter.Text(root,width=8,height=1, font=20)
    text_degree.place(x=180,y=150)   
    text_degree.delete('1.0', tkinter.END)

    #Outlook Text
    text_outlook=tkinter.Text(root,width=37,height=1, font=20)
    text_outlook.place(x=350,y=150)   
    text_outlook.delete('1.0', tkinter.END)

    #Exchange Rate Text
    text_exchange=tkinter.Text(root,width=10,height=1, font=20)
    text_exchange.place(x=180,y=250)   
    text_exchange.delete('1.0', tkinter.END)

    #Brent Index Rate Text
    text_brent=tkinter.Text(root,width=10,height=1, font=20)
    text_brent.place(x=180,y=350)   
    text_brent.delete('1.0', tkinter.END)

    #wti Index Rate Text
    text_wti=tkinter.Text(root,width=10,height=1, font=20)
    text_wti.place(x=480,y=350)   
    text_wti.delete('1.0', tkinter.END)

    #Gold Index Rate Text
    text_gold=tkinter.Text(root,width=15,height=1, font=20)
    text_gold.place(x=80,y=450)   
    text_gold.delete('1.0', tkinter.END)

    #Bitcoin Index Rate Text  
    text_bitcoin=tkinter.Text(root,width=10,height=1, font=20)
    text_bitcoin.place(x=480,y=450)   
    text_bitcoin.delete('1.0', tkinter.END)
    
    #PM 2.5 Text  
    text_pm=tkinter.Text(root,width=10,height=1, font=20)
    text_pm.place(x=180,y=550)   
    text_pm.delete('1.0', tkinter.END)

    #Level Text  
    text_level=tkinter.Text(root,width=35,height=1, font=20)
    text_level.place(x=360,y=550)   
    text_level.delete('1.0', tkinter.END)
    
    #///////////////////////////////////////////////////////////////////    
    
    
    def normal_display():       
        #///////Datetime Text//////////////////////////////////////        
        text_datetime.delete('1.0', tkinter.END)
        text_datetime.insert('1.0', 0)   
        text_datetime.insert('1.0',str(t))

        #///////Degree Text//////////////////////////////////////        
        text_degree.delete('1.0', tkinter.END)
        text_degree.insert('1.0', 0)   
        text_degree.insert('1.0',degree)

        #//////Outlook Text///////////////////////////////////////        
        text_outlook.delete('1.0', tkinter.END)
        text_outlook.insert('1.0', '')   
        text_outlook.insert('1.0',outlook)

        #///////Exchange Rate Text//////////////////////////////////////       
        text_exchange.delete('1.0', tkinter.END)
        text_exchange.insert('1.0', 0)   
        text_exchange.insert('1.0',exchange)

        #///////Brent Index Rate Text//////////////////////////////////////        
        text_brent.delete('1.0', tkinter.END)
        text_brent.insert('1.0', 0)   
        text_brent.insert('1.0',brent)

        #///////wti Index Rate Text//////////////////////////////////////       
        text_wti.delete('1.0', tkinter.END)
        text_wti.insert('1.0', 0)   
        text_wti.insert('1.0',wti)

        #///////Gold Index Rate Text//////////////////////////////////////        
        text_gold.delete('1.0', tkinter.END)
        text_gold.insert('1.0', 0)   
        text_gold.insert('1.0',gold)

        #///////Bitcoin Index Rate Text///////////////////   
        text_bitcoin.delete('1.0', tkinter.END)
        text_bitcoin.insert('1.0', 0)   
        text_bitcoin.insert('1.0',bitcoin)

        #///////PM 2.5 Index Rate Text///////////////////   
        text_pm.delete('1.0', tkinter.END)
        text_pm.insert('1.0', 0)   
        text_pm.insert('1.0',pm)

        #///////Level Text///////////////////   
        text_level.delete('1.0', tkinter.END)
        text_level.insert('1.0', '')   
        text_level.insert('1.0',level)
   
    def refresh():
       get()
       normal_display()

    refresh()
    
    def about_spider():
        about_root=tkinter.Tk()
        about_root.geometry('300x200+300+40')
        about_root.title('About Spider')
    
        label_author=tkinter.Label(about_root,text='Author: Chuan Yang', font=30)
        label_author.place(x=50,y=30)

        label_author=tkinter.Label(about_root,text='March 2015 in Houston, TX', font=30)
        label_author.place(x=50,y=80)

        button_refresh=tkinter.Button(about_root, width=15, height=2, text='OK', font=20, command=about_root.destroy)
        button_refresh.place(x=80, y=125)

        about_root.mainloop()
        
    #Refresh Button
    button_refresh=tkinter.Button(root, width=15, height=2, text='Refresh', font=20, command=refresh)
    button_refresh.place(x=70, y=610)

    #About Button
    button_about=tkinter.Button(root, width=15, height=2, text='About', font=20, command=about_spider)
    button_about.place(x=280, y=610)

    #Exit Button
    button_refresh=tkinter.Button(root, width=15, height=2, text='Exit', font=20, command=root.destroy)
    button_refresh.place(x=510, y=610)
    
    root.mainloop()
   
