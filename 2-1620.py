for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            if not((not x or y or z) and (not x or not z)):
                print(y, z, x)