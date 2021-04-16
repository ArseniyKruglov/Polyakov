for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            if (not x or y) and (not y or z):
                f = 1
            else:
                f = 0
                
            print(y, x, z, ' ', f)
