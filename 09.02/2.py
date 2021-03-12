for i in range (0, 2 ** 4):
    w = True if (i % 2 == 0) else False
    i //= 2

    z = True if (i % 2 == 0) else False
    i //= 2

    y = True if (i % 2 == 0) else False
    i //= 2

    x = True if (i % 2 == 0) else False
    i //= 2

    if ((not y or x) or (not z and w)) == (w == x):
        F = True
    else:
        F = False

    w = 1 if w else 0
    z = 1 if z else 0
    y = 1 if y else 0
    x = 1 if x else 0
    F = 1 if F else 0

    if (F):
        print(x, y, z, w, ' ', F)
