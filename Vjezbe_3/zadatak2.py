from particle import Particle
import matplotlib.pyplot as plt
import numpy as np

p1 = Particle()

dx = np.linspace(0.01, 1, 100)

D_analiticki = 10**2 * np.sin(2*((60/360)*2*np.pi)) / 9.81

x = []
y = []

for i in dx:

    p1.set_initial_conditions(0, 0, 10, 60, i)
    x.append(p1.range())
    y.append((abs(x[-1] - D_analiticki) / D_analiticki)*100)
    p1.reset()

plt.plot(dx, y)
plt.show()