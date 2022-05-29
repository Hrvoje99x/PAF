import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import domaci_5.em as em 

p = em.EM(1, 1, np.array((0.1, 0.1, 0.1)), np.array((0 ,0, 1)), np.array((0 ,0, 0)), np.array((0, 0, 0)), 0.01)
p.Euler(20)

e = em.EM(-1 ,1, np.array((0.1, 0.1, 0.1)), np.array((0, 0, 1)), np.array((0, 0, 0)), np.array((0, 0, 0)), 0.01)
e.Euler(20)

ax = plt.axes(projection = '3d')
ax.plot3D(e.x_, e.y_, e.z_)
ax.plot3D(p.x_, p.y_, p.z_)
plt.show()