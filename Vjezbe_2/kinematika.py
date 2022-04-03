import matplotlib.pyplot as plt
import numpy as np

class Kinematika:

    def __init__(self):

        self.X = []
        self.Y = []
        self.S = []
        self.V = []
        self.A = []

        self.dt = 0.01
        self.g = -9.81
        self.a = 0

    def jednoliko(self, F, m):

        self.F = F
        self.m = m

        a = F/m
        v = 0
        s = 0

        t = np.linspace(0, 10, 100)

        for i in t:

            v = v + a*self.dt
            s = s + v*self.dt

            self.V.append(v)
            self.S.append(s)
            self.A.append(a)

        plt.plot(t, self.S)
        plt.xlabel("t [s]")
        plt.ylabel("s [m]")
        plt.show()

        plt.plot(t, self.V)
        plt.xlabel("t [s]")
        plt.ylabel("v [m/s]")
        plt.show()

        plt.plot(t, self.A)
        plt.xlabel("t [s]")
        plt.ylabel("a [m/s**2]")
        plt.show()

    def kosi_hitac(self, v0, theta):

        self.v0 = v0
        self.theta = theta

        theta = (theta/360)*2*np.pi
        vx = np.cos(theta)*v0
        vy = np.sin(theta)*v0
        x = 0
        y = 0
        t = np.linspace(0, 10, 100)

        for i in t:

            vx = vx + self.a*self.dt
            vy = vy + self.g*self.dt
            x = x + vx*self.dt
            y = y + vy*self.dt

            self.X.append(x)
            self.Y.append(y)

        plt.plot(self.X, self.Y)
        plt.xlabel("x [m]")
        plt.ylabel("y [m]")
        plt.show()

        plt.plot(t, self.X)
        plt.xlabel("t [s]")
        plt.ylabel("x [m]")
        plt.show()

        plt.plot(t, self.Y)
        plt.xlabel("t [s]")
        plt.ylabel("y [m]")
        plt.show()