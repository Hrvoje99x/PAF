import sila as prt

def f1(x,v,t):
    f = 100
    return f 

def f2(x,v,t):
    k = 20
    f = -k*x
    return f 

p1 = prt.Particle(10,0,10,f1)
p1.plot_trajectory(0.01,5)

p2 = prt.Particle(10,0,10,f2)
p2.plot_trajectory(0.01,5)