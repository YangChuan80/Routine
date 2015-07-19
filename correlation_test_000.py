import scipy.stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

leadb=[0.11, 0.25, 0.23, 0.24, 0.26, 0.09, 0.25, 0.06, 0.23, 0.33, 0.15, 0.04, 0.20, 0.34, 0.22]
leadu=[0.14, 0.25, 0.28, 0.25, 0.28, 0.10, 0.27, 0.09, 0.24, 0.30, 0.16, 0.05, 0.20, 0.32, 0.24]

combo=[leadb,leadu]
df=pd.DataFrame(combo)

t=scipy.stats.linregress(leadb,leadu)

plt.scatter(leadb,leadu)


x=np.arange(0,0.35, 0.001)

y=t[0]*x+t[1]

plt.plot(x,y,color='r')


print('The Slope is: %s\n'%t[0])
print('The Intercept is: %s\n'%t[1])
print('The Correlation Coefficient is %s\n'%t[2])

