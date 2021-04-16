for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            print(y, x, z, ' ', 1 if (not x or y) and (not y or z) else 0)
