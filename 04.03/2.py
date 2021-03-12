for i in range(0, 2 ** 4):
    w = i % 2
    z = i // 2 % 2
    y = i // 2 // 2 % 2
    x = i // 2 // 2 // 2 % 2

    if not x and y and z or x and not y and not x:
        F = 1
    else:
        F = 0

    print(x, y, z, w, ' ', F)
