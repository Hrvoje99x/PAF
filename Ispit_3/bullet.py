import math
import matplotlib.pyplot as plt

class Bullet:

    def __init__(self, height, speed):
        self.x = [0]
        self.y = [height]
        self.vx = [speed]
        self.vy = [0]
        self.t = [0]
        self.g = -9.81
        self.dt = 0.01
        self.__print_info()

    def __print_info(self):
        print('pocetna visina: {}\npocetna brzina: {}\n'.format(self.y[-1], self.vx[-1]))

    def change_speed(self, change):
        self.vx.append(self.vx[-1]+change)

    def change_hight(self, change):
        self.y.append(self.y[-1]+change)

    def info(self):
        print('trenutna visina: {}\ntrenutna brzina: {}\n'.format(self.y[-1], self.vx[-1]))

    def __move(self):
        self.t.append(self.t[-1]+self.dt)
        self.vx.append(self.vx[-1])
        self.vy.append(self.vy[-1]+self.g*self.dt)
        self.x.append(self.x[-1]+self.vx[-1]*self.dt)
        self.y.append(self.y[-1]+self.vy[-1]*self.dt)

    def plot_graphs(self):
        while self.y[-1] >= 0:
            self.__move()

        fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 6), dpi=80)
        plt.subplots_adjust(wspace=0.4, hspace=0.5)
        plt.rcParams.update({'font.size': 8})
        plt.axis('equal')
        axes[0].plot(self.x, self.y, 'b')
        axes[0].set_xlabel('x  [$m$]') 
        axes[0].set_ylabel('y  [$m$]')
        axes[0].grid(lw=0.5)
        axes[0].axis('tight')
        axes[0].set_title('x-y graf')
        axes[1].plot(self.t, self.x, 'r')
        axes[1].set_xlabel('t  [$s$]')
        axes[1].set_ylabel('x  [$m$]')
        axes[1].grid(lw=0.5)
        axes[1].axis('tight')
        axes[1].set_title('x-t graf')
        axes[2].plot(self.t, self.y, 'g')
        axes[2].set_xlabel('t  [$s$]')
        axes[2].set_ylabel('y  [$m$]')
        axes[2].grid(lw=0.5)
        axes[2].axis('tight')
        axes[2].set_title('y-t graf')
        return plt.show()

    def set_dt(self, dt):
        self.dt =dt  

    def speed_to_hit_target(self, distance, height, y0, size):
        self.x = [0.]
        self.y = [y0]
        speed = []
        v = 0.
        while v <= 250:
            bum = False
            self.vx = []
            self.vx = [v]
            while self.y[-1] >= 0:
                self.__move()
                x = abs(self.x[-1]-distance)
                y = abs(self.y[-1]-height)
                if y <= size:
                    bum = True
            if bum == True:
                speed.append(v)
            v += 1
        if len(speed) == 0:
            print('Promijenite parametre.')
        else:
             print(sum(speed)/len(speed))
