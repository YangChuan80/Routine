import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame, Series

fig=plt.figure()
img=fig.add_subplot(1,1,1)

circ=plt.Circle((0.7,0.2),0.15,color='b',alpha=0.3)

img.add_patch(circ)

