for A in range(1, 10000):
    ok = True

    for x in range(1, 1000):
        if not( not(x % 18 == 0) or (not(x % 54 == 0) or (x % A == 0)) ):
            ok = False
            break

    if ok:
        print(A)