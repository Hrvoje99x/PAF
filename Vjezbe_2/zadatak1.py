import matplotlib.pyplot as plt
import numpy as np

def jednoliko(F, m):

    dt = 0.01
    n = 100
    a = F/m
    v = 0
    x = 0

    X = []
    V = []
    A = []
    T = []

    for i in range(n):

        v = v + a*dt
        x = x + v*dt

        V.append(v)
        X.append(x)
        A.append(a)
        T.append(i*dt)

    plt.plot(T, X)
    plt.xlabel("t [s]")
    plt.ylabel("x [m]")
    plt.show()

    plt.plot(T, V)
    plt.xlabel("t [s]")
    plt.ylabel("v [m/s]")
    plt.show()

    plt.plot(T, A)
    plt.xlabel("t [s]")
    plt.ylabel("a [m/s**2]")
    plt.show()

jednoliko(10, 5)