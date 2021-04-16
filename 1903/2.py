for i in range(0, 2 ** 4):
    w = i % 2
    z = i // 2 % 2
    y = i // 4 % 2
    x = i // 8 % 2

    if not(not(x != z) or ((x or w) == y)):
        print(x, w, y, z)
    
