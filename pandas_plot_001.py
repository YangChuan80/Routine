import numpy as np
from pandas import DataFrame, Series
import matplotlib.pyplot as plt

fig=plt.figure()
ax1=fig.add_subplot(1,1,1)

df=DataFrame(np.random.randn(30).reshape(6,5),
             columns=['First','Second','Third','Forth','Fifth'])
df=abs(df)

df.plot(ax=ax1,kind='barh',ylim=[0,7.5],stacked=True)
