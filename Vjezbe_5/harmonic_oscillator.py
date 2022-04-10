import numpy as np
import matplotlib.pyplot as plt

class HarmonicOscillator():

    def __init__(self, k, m, dt = 0.01):

        self.x = [0]
        self.v = [0]
        self.a = [0]
        self.t = [0]

        self.k = k
        self.m = m
        self.dt = dt

    def reset(self):

        self.__init__()

    def __move(self):

        self.a.append(- (self.k * self.x[-1]) / self.m)
        self.v.append(self.v[-1] + self.a[-1]*self.t[-1])
        self.x.append(self.x[-1] + self.v[-1]*self.t[-1])
        self.t.append(self.t[-1] + self.dt)

    def osciliranje(self):

        for i in range(int(100*self.dt)):

            self.__move()


    def plot(self):

        plt.plot(self.x, self.t)
        plt.show()

        plt.plot(self.v, self.t)
        plt.show()

        plt.plot(self.a, self.t)
        plt.show()   