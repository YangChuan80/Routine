import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


df=pd.read_csv('D:\\Database\\Matrix_00.csv')
df=df.set_index('PID')

patient_id=list(df.index)
group=list(df.columns)

mx=pd.DataFrame(np.array(df))

xvalue=len(df.columns)
yvalue=len(df.index)

product=xvalue*yvalue

#Recombinate the dataframe
df1d=mx.stack().reset_index()

df1d.columns=['y','x','vaules']

#Create the figure object
fig=plt.figure()

plt.axis([-0.5,xvalue-0.5,yvalue-0.5,-0.5])

#Subplot ax
ax0=fig.add_subplot(1,1,1)


#Normalization
normalized=4*df.max().max()

#Plot
for i in range(product):
    if df1d.x.ix[i]<xvalue//2:
        circle_color='r'
    elif df1d.x.ix[i]>=xvalue//2:
        circle_color='b'
        
    circle=plt.Circle((df1d.x.ix[i],df1d.y.ix[i]),
                      radius=math.sqrt(df1d.icol(2).irow(i)/normalized),
                      color=circle_color)
    ax0.add_patch(circle)


#plt.grid()
#plt.title('Matrix Plot')

ax0.set_yticks([y for y in range(yvalue)])
ax0.set_yticklabels(patient_id,fontsize=18)

ax0.set_xticks([xvalue//4, xvalue*3//4])
ax0.set_xticklabels(['Lidocaine', 'Amiodarone 323'],
                    fontsize=20)

plt.subplots_adjust(left=0.21, right=0.99,
                    bottom=0.05, top=0.99)


plt.show()


#Export
fig.savefig('D:\\Database\\export_image.png',dpi=600)

