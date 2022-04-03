import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self):
        
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.t = []
        self.vmax = []
        
        self.g = 9.81
        self.a = 0

    def set_initial_conditions(self, x0, y0, v0, theta, dt = 0.01):

        self.x0 = x0
        self.y0 = y0
        self.v0 = v0
        self.dt = dt
        self.theta = (theta/360)*2*np.pi

        self.t.append(0)
        self.x.append(x0)
        self.y.append(y0)
        self.vx.append(v0*np.cos(self.theta))
        self.vy.append(v0*np.sin(self.theta))

    def reset(self):
        self.__init__()

    def __move(self):

        self.t.append(self.t[-1] + self.dt)
        self.vx.append(self.vx[-1] + self.a*self.dt)
        self.vy.append(self.vy[-1] - self.g*self.dt)
        self.x.append(self.x[-1] + self.vx[-1]*self.dt)
        self.y.append(self.y[-1] + self.vy[-1]*self.dt)
        self.vmax.append(np.sqrt(self.vx[-1]**2 + self.vy[-1]**2))
        #print(self.x[-1])
        #print(self.t[-1])
        #print(self.vmax[0])

    def range(self):
        
        while self.y[-1] >= 0:
            self.__move()
        return self.x[-1]

    def plot_trajectory(self):

        plt.plot(self.x, self.y)
        plt.show()

    def total_time(self):

        while self.y[-1] >= 0:
            self.__move()
        return self.t[-1]

    def max_speed(self):
        
        while self.y[-1] >= 0:
            self.__move()
        return self.vmax[0]


        
