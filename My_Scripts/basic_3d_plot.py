import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes(projection = "3d")
#ax.set_zlim3d(-8,8) 
res = 30
base = -3
max = 3
step = 0.1

x, y = np.meshgrid(np.arange(base,max,step), np.arange(base,max,step))
z = np.sin(x+y)

ax.plot_surface(x,y,z, rcount = res, ccount = res, cmap = "plasma")
plt.show()