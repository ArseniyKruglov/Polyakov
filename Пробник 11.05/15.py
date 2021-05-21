for A in range(1, 10000):
    ok = True

    for x in range(1, 100000):
        if not( ((x % 19 != 0) or (x % 15 != 0)) <= (x % A != 0) ):
            ok = False
            break

    if ok:
        print(A)
        break
