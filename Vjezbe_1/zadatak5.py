import matplotlib.pyplot as plt
import numpy as np

def f(): 
    
    x1 = int(input("x1: "))
    x2 = int(input("x2: "))
    y1 = int(input("y1: "))
    y2 = int(input("y2: "))

    #y = mx + b

    m = (y2 - y1) / (x2 - x1)
    b = y1 - m*x1

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

f()
    
    
    
