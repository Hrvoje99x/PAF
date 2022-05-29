import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import em as em 

def const_B(t):

    Bx = 0
    By = 0
    Bz = 1

    return np.array((Bx,By,Bz))

def promjenjivo_B(t):

    Bx = 0
    By = 0
    Bz = t/10

    return np.array((Bx,By,Bz))

e = em.EM(-1, 1, np.array((0.1,0.1,0.1)), const_B, np.array((0,0,0)), np.array((0,0,0)), 0.01)
x,y,z = e.Euler(20)

e.reset()

e = em.EM(-1, 1, np.array((0.1,0.1,0.1)), promjenjivo_B, np.array((0,0,0)), np.array((0,0,0)), 0.01)
x2,y2,z2 = e.Euler(20)
ax = plt.axes(projection = '3d')
ax.plot3D(x, y, z)
ax.plot3D(x2, y2, z2, '-.')
plt.show()

p = em.EM(1,1,np.array((0.1,0.1,0.1)),promjenjivo_B,np.array((0,0,0)),np.array((0,0,0)),0.01)
xp,yp,zp = p.Euler(20)

ax = plt.axes(projection='3d')
ax.plot3D(x2,y2,z2)
ax.plot3D(xp,yp,zp, '-.')
plt.show()