for A in range (1, 100000):
    ok = True
    for x in range (1, 1000):
        if not(not((x % A == 0) and (x % 24 == 0) and not(x % 16 == 0)) or not(x % A == 0)):
            ok = False
            break

    if (ok):
        print(A)
        break
