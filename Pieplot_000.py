import matplotlib.pyplot as plt
import numpy as np

l=[35,45,10,30,100,70]
ex=[0,0,0,0.2,0,0]

plt.pie(l,explode=ex,shadow=True)

plt.bar(np.arange(len(l)),l)

plt.show()
