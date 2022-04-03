import numpy as np

def derivacija(f, x, h = 0.01, m = 0):

    if m == 1:
        #print((f(x + h) - f(x)) / h)
        return(f(x + h) - f(x)) / h

    elif m == 0:
        #print((f(x + h) - f(x)) / 2*h)
        return(f(x + h) - f(x)) / 2*h


#derivacija(np.cos, 0, 1e-8, 1)

def derivacija2(f,x1, x2, h = 0.01, m = 0):

    d = []
    dx = np.arange(x1, x2, h)

    for i in dx:

        if m == 0:
            d.append(derivacija(f, i, h))

        elif m == 1:
            d.append(derivacija(f, i, h, 1))

    return d, dx

#derivacija2(np.cos, -2, 2, 0.01)

def integracija(f, a, b, n):

    dx = (b-a)/n
    
    x_gornja = a
    x_donja = a + dx

    gm = 0
    dm = 0

    for i in range (n):

        gm = f(x_gornja)*dx
        dm = f(x_donja)*dx

        x_gornja += x_gornja
        x_donja += x_donja

        print(gm, dm)

    return gm, dm

#integracija(np.cos, 0, 5, 100)

def integracija2(f, a, b, n):

    dx = (b-a)/n
    xk = a
    suma = 0

    for i in range(n):

        suma = suma + f(xk + f(xk + dx))
        xk = xk + dx

    integral = (dx/2)* suma
    print(integral)

integracija2(np.cos, 0, 1, 100)


