import scipy.stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

standards=pd.read_csv('.\\Standards.csv')

regress_results=scipy.stats.linregress(standards['concentration'], standards['hep avg'])
corr_results=standards['concentration'].corr(standards['hep avg'])

print('Regression results are: ',regress_results,'\n')
print('Correlation results are: ',corr_results)

#Plot
x=np.arange(min(standards['concentration'])-10,max(standards['concentration'])+10)
y=regress_results[0]*x+regress_results[1]

plt.scatter(standards['concentration'], standards['hep avg'])
plt.plot(x,y,color='r')
plt.title('hep')
plt.show()
