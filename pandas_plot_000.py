from pandas import DataFrame, Series
import numpy as np

df=DataFrame(np.random.randn(10,4).cumsum(0),
             columns=['A','B','C','D'],
             index=np.arange(0,100,10),
             )

df=abs(df*100)

img=df.plot(kind='bar',title='Pandas Plot')

