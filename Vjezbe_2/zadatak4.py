import matplotlib.pyplot as plt
import numpy as np

g = 9.81
dt = 0.01

def hitac(v0, theta):
    theta = (theta/360)*2*np.pi
    vx = v0*np.cos(theta)
    vy = v0*np.sin(theta)
    tmax = 2*v0*np.sin(theta)/g

    x = [0]
    y = [0]
    

    for i in range(int(tmax*100)):
        vy = vy - g*dt
        y[i] = y[i] + vy*dt
        x[i] = x[i] + vx*dt

        y.append(y[i])
        x.append(x[i])
        


    plt.plot(x, y)
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    plt.show()

hitac(15, 45)

def max_visina(v0, theta):
    theta = (theta/360)*2*np.pi
    vy = v0*np.sin(theta)
    tmax = 2*v0*np.sin(theta)/g

    Y = [0]

    for i in range(int(tmax*100)):
        vy = vy - g*dt
        Y[i] = Y[i] + vy*dt
        Y.append(Y[i])

        if vy <= 0:
            break

    print(Y[-1])

max_visina(15,45)

def domet(v0, theta):

    theta = (theta/360)*2*np.pi
    vx = v0*np.cos(theta)
    vy = v0*np.sin(theta)
    tmax = 2*v0*np.sin(theta)/g

    X = [0]
    Y = [0]

    for i in range(int(tmax*100)):

        vy = vy - g*dt
        Y[i] = Y[i] + vy*dt
                
        Y.append(Y[i])

        if Y[i] >= 0:

            X[i] = X[i] + vx*dt
            X.append(X[i])

        else:
            break

    print(X[-1])

domet(15, 45)

def max_brzina(v0, theta):

    theta = (theta/360)*2*np.pi
    vx = v0*np.cos(theta)
    vy = v0*np.sin(theta)
    tmax = 2*v0*np.sin(theta)/g
    
    v = 0
    V = [0]

    for i in range(int(tmax*100)):

        vy = vy - g*dt
        v = np.sqrt(vx**2 + vy**2)
        
        V.append(v)

    print(V[1])

max_brzina(15, 45)

def meta(v0, theta, x0, y0, r):

    theta = (theta/360)*2*np.pi
    vx = v0*np.cos(theta)
    vy = v0*np.sin(theta)
    tmax = 2*v0*np.sin(theta)/g

    x = [0]
    y = [0]

    hit = False
    
    blizu = np.sqrt(x0**2 + y0**2)

    for i in range(int(tmax*100)):

        vy = vy - g*dt
        y[i] = y[i] + vy*dt
        
        if y[i] >= 0:

            x[i] = x[i] + vx*dt

            y.append(y[i])
            x.append(x[i])

            p = x[i] - x0
            q = y[i] - y0

            if p**2 + q**2 <= r**2:

                hit = True

            else:

                d = np.sqrt(p**2 + q**2) - r
                blizu = d

        else:
            break

    if hit == True:

        print('Meta je pogođena')

    else:

        print('Meta nije pogođena. Najmanja udaljenost od mete je {}m'.format(blizu))

    target = np.linspace(0, 2*np.pi, 100)
    t1 = x0 + r*np.cos(target)
    t2 = y0 + r*np.sin(target)
    plt.plot(t1, t2)

    plt.plot(x, y)
    plt.xlabel("x [m]")
    plt.ylabel("y [m]")
    plt.show()

meta(15, 45, 5, 2, 1)