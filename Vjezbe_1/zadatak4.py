def f(): 
    
    x1 = int(input("x1: "))
    x2 = int(input("x2: "))
    y1 = int(input("y1: "))
    y2 = int(input("y2: "))

    #y = mx + b

    m = (y2 - y1) / (x2 - x1)
    b = y1 - m*x1

    print("y =", m,"* x +", b)

f()
