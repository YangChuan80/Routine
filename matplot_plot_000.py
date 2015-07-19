import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame, Series

fig,img=plt.subplots(1,1)

#img.plot(np.random.randn(100),color='red',
  #       linestyle='dashed',marker='o')

plt.plot(np.random.randn(100),color='red',label='Red One')
plt.plot(np.random.randn(100),color='green',label='Green One')
plt.plot(np.random.randn(100),color='blue',label='Blue One')

plt.set_title('Colorful Lines',fontsize=20)
plt.set_xlabel('Frequency Level',fontsize=18)

plt.legend(loc='best')

#img[0,2].plot([30,100,20,80,120],'ko--',color='purple')

#img.scatter(np.random.randn(100),np.random.randn(100)*2,color='red')
