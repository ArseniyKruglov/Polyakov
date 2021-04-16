for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            if not(not(not x or not z) or (x == y)):
                print(z, x, y, ' ', 0)
