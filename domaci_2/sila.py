import matplotlib.pyplot as plt
import numpy as np

def sila(f,x0,v0,t_end,masa,dt = 0.1,t_start=0):
    res = []
    t = t_start

    f0 = f(x0,v0,t)
    res.append(f0)

    a0 = f0/masa

    while t <= t_end:
        t += dt
        v0 = v0 + a0 * dt
        x0 = x0 + v0 * dt

        f0 = f(x0,v0,t)

        a0 = f0/masa

        res.append(f0)

    return res


def f(x,v,t):
    k = 10
    return -k*x

res = sila(f, 0, 10, 10, 1)
print(res)
