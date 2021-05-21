for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (not w or z) and ((not y or x) == (not z or y)):
                    print(x, w, z, y, ' ', 1)
