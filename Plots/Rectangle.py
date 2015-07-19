import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.patches import Rectangle

#Create the figure object
fig=plt.figure()

plt.axis([-0.7,20,30,-0.7])

#Subplot ax
ax0=fig.add_subplot(1,1,1)

#currentAxis = plt.gca()
ax0.add_patch(Rectangle((1, 2), 10, 10, linewidth=0, facecolor="blue"))
ax0.add_patch(Rectangle((1, 2), 8, 10, linewidth=0, facecolor="red"))

plt.show()
