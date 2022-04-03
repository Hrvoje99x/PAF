import numpy as np
import matplotlib.pyplot as plt
import calculus 

def f(x):
    s = np.linspace(0, 10, 10)
    for i in s:

        calculus.integracija(i**2, 0, 5, 100)