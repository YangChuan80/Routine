import numpy as np
import pandas as pd

df=pd.DataFrame(np.arange(12).reshape(4,3),
column=[['a','a','b'],
['one','one','two']])

for i in range(3):
