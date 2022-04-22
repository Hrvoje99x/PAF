import matplotlib.pyplot as plt
import numpy as np

class ProjectileDrop:

    def __init__(self, h, vx):

        self.h = h
        self.vx = vx

    def printinfo(self):
        print('Visina na kojoj se nalazi avion {}, iznos horizontalne brzine aviona {}'.format(self.h, self.vx))

    def promjena_visine(self, nova_h):

        self.h = nova_h
        return self.h
        

    def promjena_vx(self, novi_vx):

        self.vx = novi_vx
        return self.vx

    def izbacaj(self):

        self.g = 9.81
        self.dt = 0.01

        self.dh = []
        self.dx = [0]
        self.dvy = [0]
        self.t = [0]

        self.dh.append(self.h)

        while self.dh[-1] >= 0:

            self.dvy.append(self.dvy[-1] + 1/2 * self.g * self.t[-1])
            self.dh.append(self.dh[-1] - self.dvy[-1] * self.t[-1])
            self.dx.append(self.dx[-1] + self.vx*self.t[-1])
            self.t.append(self.t[-1]+self.dt)

        return self.dh, self.dx, self.dvy, self.t

    def plot(self):

        plt.plot(self.dx, self.dh)
        plt.xlabel('domet [m]')
        plt.ylabel('visina [m]')
        plt.show()

        plt.plot(self.t, self.dvy)
        plt.xlabel('t [s]')
        plt.ylabel('vy [m/s]')
        plt.show()

    def vrijeme_pada(self):

        g = 9.81

        self.dh2 = []
        self. dh2.append(self.h)
        self.t2 = [0]
        self.dvy2 = [0]
        self.tmax = []

        self.dt2 = np.linspace(0.001, 0.1, 100)

        for i in self.dt2:

            while self.dh2[-1] >= 0:

                self.dvy2.append(self.dvy2[-1] + g * self.t2[-1])
                self.dh2.append(self.dh2[-1] - self.dvy2[-1] * self.t2[-1])
                self.t2.append(self.t2[-1] + i)

            self.tmax.append(self.t2[-1])

        return self.tmax

    def plot2(self):

        plt.plot(self.dt2, self.tmax)
        plt.xlabel('vrijeme pada [s]')
        plt.ylabel('dt [s]')
        plt.show()

    def meta(self, x_mete, x_mete2, v_vjetar):

        dt = 0.01

        self.x_mete = x_mete
        self.x_mete2 = x_mete2
        self.v_vjetar = v_vjetar

        v = self.vx + self.v_vjetar

        self.dx2 = [0]
        self.t3 = [0]

        self.dx.append(self.dx2[-1] + self.vx*self.t3[-1])
        self.t.append(self.t2[-1] + dt)

        







