import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.DataFrame(np.random.randn(30).reshape(6,5),
                index=[['First','Second','Third','Fourth','Fifth','Sixth'],
                       ['Odd','Even','Odd','Even','Odd','Even']],
                columns=[['d1','d2','d3','d4','d5'],
                         ['txt','bin','txt','asc','bin']])
df.index.names=['id','qua']
df.columns.names=['department','type']
