import matplotlib.pyplot as plt
import numpy as np

def f(x1, x2, y1, y2): 

    #y = mx + b

    m = (y2 - y1) / (x2 - x1)
    b = -m*x1 + y1

    x = np.linspace(-10, 10, 200)

    y = m*x + b

    naziv = input("Naziv grafa: ")
    
    plt.plot(x, y, '-r')
    plt.title(naziv)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(linewidth = 3, color = 'b')
    plt.axvline(linewidth = 3, color = 'b')
    plt.grid()
    
    odabir = input("Spremanje grafa? DA/NE: ")
    
    if odabir == "DA":
        plt.savefig('graf.pdf')
    elif odabir == "NE":
        plt.show()

f(3, 7, 2, 4)
    
    
    
