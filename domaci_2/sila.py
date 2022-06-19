import matplotlib.pyplot as plt

class Particle:

    def __init__(self, m, x0, v0, func):

        self.x_l = []
        self.v_l = []
        self.a_l = []
        self.t_l = []
        self.m = m
        self.x = x0
        self.v = v0
        self.F = func
        self.t = 0
        self.a = self.F(self.x,self.v,self.t)/self.m
        self.x_l.append(self.x)
        self.v_l.append(self.v)
        self.a_l.append(self.a)
        self.t_l.append(self.t)

    def move(self, dt, t):

            N = int(t/dt)

            for i in range(N):

                self.a = self.F(self.x,self.v,self.t)/self.m
                self.v = self.v + self.a*dt
                self.x = self.x + self.v*dt
                self.t += dt
                self.x_l.append(self.x)
                self.v_l.append(self.v)
                self.a_l.append(self.a)
                self.t_l.append(self.t)
            return self.x_l,self.v_l,self.a_l,self.t_l

    def plot_trajectory(self, dt, t):

        x,v,a,t = self.move(dt, t)
        plt.subplot(1,3,1)
        plt.plot(t,x)
        plt.subplot(1,3,2)
        plt.plot(t,v)
        plt.subplot(1,3,3)
        plt.plot(t,a)
        plt.show()
    
    def reset(self):

        del self.k
        del self.m
        del self.x
        del self.v
        del self.a
        del self.t
        del self.x_l
        del self.v_l
        del self.a_l
        del self.t_l
