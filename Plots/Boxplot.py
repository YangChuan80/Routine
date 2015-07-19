from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import matplotlib.pylab as plt

df=DataFrame(abs(np.random.randn(30).reshape(6,5)))
fig1=plt.figure()
ax1=fig1.add_subplot(1,1,1)

plt.boxplot(df[0])

plt.show()
