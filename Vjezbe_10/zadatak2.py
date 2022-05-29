import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import em as em 

e = em.EM(-1,1,np.array((0.1,0.1,0.1)),np.array((0,0,1)),np.array((0,0,0)),np.array((0,0,0)),0.01)
x,y,z = e.Euler(20)
e.reset
e = em.EM(-1,1,np.array((0.1,0.1,0.1)),np.array((0,0,1)),np.array((0,0,0)),np.array((0,0,0)),0.01)
x2,y2,z2 = e.RK(20)

ax = plt.axes(projection='3d')
ax.plot3D(x,y,z)
ax.plot3D(x2,y2,z2, '-.')
plt.show()