import numpy as np
from pandas import DataFrame, Series
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats

df=DataFrame(abs(np.random.randn(30).reshape(6,5))*100)

plt.bar(np.arange(len(df.mean())), df.mean(),        
        align='center',
        color='white',        

        yerr=df.std(),
        ecolor='black',
        capsize=5,
        linewidth=1,)
plt.grid()

plt.show()
