for i in range (0, 2 ** 4):
    w = True if (i % 2 == 1) else False
    i //= 2

    z = True if (i % 2 == 1) else False
    i //= 2

    y = True if (i % 2 == 1) else False
    i //= 2

    x = True if (i % 2 == 1) else False
    i //= 2
    
    if (x or y) and not (y == z) and not w:
        F = 1
    else:
        F = 0

    x = 1 if x else 0
    y = 1 if y else 0
    z = 1 if z else 0
    w = 1 if w else 0

    if (F == 1):
        print (z, y, x, w, ' ', F)
    
