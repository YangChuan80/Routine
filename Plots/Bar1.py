import numpy as np
from pandas import DataFrame, Series
import pandas as pd
import matplotlib.pyplot as plt

df=DataFrame(abs(np.random.randn(30).reshape(6,5))*100)

plt.bar(np.arange(len(df.mean())), df.mean(),
        align='center',
        color='white',
        linewidth=1.5)

plt.hold(True)

plt.errorbar(np.arange(len(df.mean())),df.mean(),df.std(),
             elinewidth=1.2,
             capsize=7.5,
             fmt=None)
plt.show()
