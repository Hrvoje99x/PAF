def f(x1, x2, y1, y2): 

    #y = mx + b

     m = (y2 - y1) / (x2 - x1)
     b = -m*x1 + y1

     print("y = {}x + {}".format(m, b))

f(3, 7, 2, 4)
