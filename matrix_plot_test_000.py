import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



#Import
df=pd.read_csv('D:\\Database\\import_file.csv',header=None)

xvalue=len(df.columns)
yvalue=len(df.index)
product=xvalue*yvalue

print(xvalue,yvalue,product)

#df=pd.DataFrame(5*abs(np.random.randn(product).reshape(yvalue,xvalue)))

#Recombinate the dataframe
df1d=df.stack().reset_index()

df1d.columns=['y','x','vaules']

#Create the figure object
fig=plt.figure()

plt.axis([0,xvalue+1,yvalue+1,0])

#Subplot ax
ax=fig.add_subplot(1,1,1)

#Normalization
normalized=2*df.max().max()

#Plot
for i in range(product):
    circle=plt.Circle((df1d.x.ix[i]+1,df1d.y.ix[i]+1),
                      radius=df1d.icol(2).irow(i)/normalized,
                      color='r')
    ax.add_patch(circle)

plt.grid()
plt.title('Matrix')
plt.show()

#Export
fig.savefig('D:\\Database\\export_image.png',dpi=600)



