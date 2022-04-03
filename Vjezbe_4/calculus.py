import numpy as np

def derivacija(f, x, h = 0.01, m = 0):

    if m == 1:
        print((f(x + h) - f(x)) / h)
        return(f(x + h) - f(x)) / h

    elif m == 0:
        print((f(x + h) - f(x)) / 2*h)
        return(f(x + h) - f(x)) / 2*h


derivacija(np.cos, 0, 1e-8, 1)
