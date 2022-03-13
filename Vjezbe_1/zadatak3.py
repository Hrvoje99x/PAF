while True:
    try:
        x1 = int(input("X1: "))
        break
    except ValueError:
        print('unesi broj')

while True:
    try:
        x2 = int(input("X2: "))
        break
    except ValueError:
        print('unesi broj')

while True:
    try:
        y1 = int(input("y1: "))
        break
    except ValueError:
        print('unesi broj')

while True:
    try:
        y2 = int(input("y2: "))
        break
    except ValueError:
        print('unesi broj')

#y = mx + b

m = (y2 - y1) / (x2 - x1)
b = y1 - m*x1

print("y =", m,"* x +", b)