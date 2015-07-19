from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s=Series(np.random.randn(30))

fig1=plt.figure()
ax1=fig1.add_subplot(1,1,1)

ax1.plot(s)
ax1.grid()

ax1.text(3,1,'Python Plot',family='Courier',fontsize=12)

ax1.set_title('Lines',family='Impact', fontsize=20)

plt.show()


