import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame, Series

fig=plt.figure()
img=fig.add_subplot(2,2,1)


#img.plot(np.random.randn(100),color='red',
  #       linestyle='dashed',marker='o')

img.plot(np.random.randn(100),color='red',label='Red One')
img.plot(np.random.randn(100),color='green',label='Green One')
img.plot(np.random.randn(100),color='blue',label='Blue One')

img.set_title('Colorful Lines',fontsize=20)
img.set_xlabel('Frequency Level',fontsize=18)

img.legend(loc='best')

img2=fig.add_subplot(2,2,2)
circle=plt.Circle((0.7,0.2),0.15,color='orange',alpha=0.3)

#img[0,2].plot([30,100,20,80,120],'ko--',color='purple')

#img.scatter(np.random.randn(100),np.random.randn(100)*2,color='red')
