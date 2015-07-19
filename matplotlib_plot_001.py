from pandas import DataFrame,Series
import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure()
img=fig.add_subplot(1,1,1)

img.plot(np.random.randn(50),color='g')

img.set_title('Hello, world!',fontsize=30)
img.set_xlabel('X Values',fontsize=18)

