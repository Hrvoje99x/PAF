import numpy as np
import matplotlib.pyplot as plt
import calculus 

def derivacija_2(f, a, b):

    r = np.linspace(a, b, 100)

    for i in range(r):

        dfx = calculus.derivacija(f(i))
        X_lista.append(i)
        dfx_lista.append(dfx)

    X_lista = []
    dfx_lista = []

    plt.plot(X_lista, dfx_lista)
    plt.show

derivacija_2(np.cos, 0, 1)