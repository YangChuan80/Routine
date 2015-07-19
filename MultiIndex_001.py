import numpy as np
import pandas as pd

df=pd.DataFrame(np.arange(12).reshape(4,3),
                columns=[['a','a','b'],
                         ['single','double','double']],
                index=[['Jan','Feb','Jun','Jun'],
                       ['bin','txt','bin','txt']])
df.columns.names=['letter','status']
df.index.names=['month','storage']


s=pd.Series(['c','d','e','f','w','e'])
s.index.name='id'

df1=pd.DataFrame(np.random.randn(30).reshape(6,5),
                 columns=['a','b','c','d','e'])
