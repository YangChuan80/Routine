from pandas import DataFrame,Series
import matplotlib.pyplot as plt
import numpy as np
import math

nd=np.random.randn(100).reshape(20,5)

df=DataFrame(nd,columns=['Dep.1','Dep.2','Dep.3','Dep.4','Dep.5'])
df=abs(df*10)

#for k in ['Dep.1','Dep.2','Dep.3','Dep.4','Dep.5']:
#    img1=df[k].plot()

#img1.set_title('Pandas Plot 1',fontsize=33)
#img1.set_xlabel('X Values')

hlines(0,0,100,color='b')
