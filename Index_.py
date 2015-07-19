import numpy as np
import pandas as pd

s=pd.Series([3,4,3,2,5])
            

s2=pd.Series([5,7,8,9,10])

s.index=s2.index=['one','two','three','four','five']
