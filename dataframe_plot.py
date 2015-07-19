import numpy as np
from pandas import DataFrame, Series
#import matplotlib.pyplot as plt

df=DataFrame(np.random.randn(30).reshape(6,5))

img=df.plot()
