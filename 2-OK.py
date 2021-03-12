for i in range(0, 2 ** 3):
    z = i // 1 % 2
    y = i // 2 % 2
    x = i // 2 // 2 % 2

    if not((not x or y or z) and (not x or not z)):
        print(y, z, x)
