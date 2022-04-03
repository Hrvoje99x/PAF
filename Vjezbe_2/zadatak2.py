from re import X
import matplotlib.pyplot as plt
import numpy as np

def kosi_hitac(v0, theta):

    theta = (theta/360)*2*np.pi
    vx = np.cos(theta)*v0
    vy = np.sin(theta)*v0

    a = 0
    g = -9.81
    x = 0
    y = 0
    dt = 0.01
    t = np.linspace(0, 10, 100)

    X = []
    Y = []

    for i in t:

        vx = vx + a*dt
        x = x + vx*dt

        vy = vy + g*dt
        y = y + vy*dt

        X.append(x)
        Y.append(y)

    plt.plot(X, Y)
    plt.xlabel("x [m]")
    plt.ylabel("y [m]")
    plt.show()

    plt.plot(t, X)
    plt.xlabel("t [s]")
    plt.ylabel("x [m]")
    plt.show()

    plt.plot(t, Y)
    plt.xlabel("t [s]")
    plt.ylabel("y [m]")
    plt.show()

kosi_hitac(15, 45)




    
