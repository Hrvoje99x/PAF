import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

class EM:

    def __init__(self, q, m, v, func, E, r, dt):

        self.q = q
        self.m= m
        self.v = v
        self.func = func
        self.E = E 
        self.r = r 
        self.dt = dt
        self.x_ = []
        self.y_ = []
        self.z_ = []
        self.x_.append(self.r[0])
        self.y_.append(self.r[1])
        self.z_.append(self.r[2])
        self.t = 0
        self.B = self.func(self.t)
    
    def reset(self):

        del self.q 
        del self.m
        del self.v 
        del self.B 
        del self.E  
        del self.r 
        del self.x_ 
        del self.y_ 
        del self.z_ 
        
    
    def akc(self, v):

        a = (self.q/self.m)*(self.E+np.cross(v,self.B))
        return a 
    
    def Euler(self, t):

        while self.t <= t:

            a = self.akc(self.v)
            self.v = self.v + a*self.dt
            self.r = self.r + self.v*self.dt
            self.B = self.func(self.t)
            self.t += self.dt
            self.x_.append(self.r[0])
            self.y_.append(self.r[1])
            self.z_.append(self.r[2])
            
        return self.x_,self.y_,self.z_
