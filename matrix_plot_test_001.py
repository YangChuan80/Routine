import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

xvalue=60
yvalue=40
product=xvalue*yvalue

df=pd.DataFrame(abs(np.random.randn(product).reshape(yvalue,xvalue)))
#df=pd.DataFrame(np.arange(256).reshape(16,16))

#Recombinate the dataframe
df1d=df.stack().reset_index()

df1d.columns=['y','x','vaules']

#Create the figure object
fig=plt.figure()

#Add subplot object:

#Subplot 1 adding
ax=fig.add_subplot(2,1,1)
plt.axis([0,xvalue+1,yvalue+1,0])
plt.grid()
plt.title('Circle Matrix')

#Subplot 2 adding
ax1=fig.add_subplot(2,1,2)
plt.axis([0,xvalue+1,yvalue+1,0])

normalized=2*df.max().max()

#Plot
for i in range(product):
    circle=plt.Circle((df1d.x.ix[i]+1,df1d.y.ix[i]+1),
                      radius=df1d.icol(2).irow(i)/normalized,
                      color='b')
    ax.add_patch(circle)

ax1=plt.pcolor(df*0.2)
plt.title('Heatmap')

plt.savefig('D:\\Database\\Image_Export.png', dpi=600)

plt.show()



