for A in range(1, 100):
    ok = True

    for x in range(1, 10000):
        if not( not((x % A == 0) and (x % 12 == 0)) or ((x % 42 == 0) or not(x % 12 == 0)) ):
            ok = False
            break

    if ok:
        print(A)
        break
