from distutils.log import info
import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self):
        
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.t = []
        
        self.dt = 0.01
        self.g = 9.81

    def set_initial_conditions(self, x0, y0, v0, theta):

        self.x0 = x0
        self.y0 = y0
        self.v0 = v0
        self.theta = (theta/360)*2*np.pi

        self.t.append(0)
        self.x.append(x0)
        self.y.append(y0)
        self.vx.append(v0*np.cos(theta))
        self.vy.append(v0*np.sin(theta))

    def reset(self):
        self.__init__()

    def __move(self):

        self.t.append(self.t[-1] + self.dt)
        self.vx.append(self.vx[-1] + self.g*self.dt)
        self.vy.append(self.vy[-1] - self.g*self.dt)
        self.x.append(self.x[-1] + self.vx[-1]*self.dt)
        self.y.append(self.y[-1] + self.vy[-1]*self.dt)

    def range(self):
        
        while self.y[-1] > 0:
            self.__move()
        return self.x[-1]

    def plot_trajectory(self):

        plt.plot(self.x, self.y)
        plt.show()



        


