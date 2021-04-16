for A in range(1, 1000):
    ok = True

    for x in range(1, 1000):
        if not((not((x % 36 == 0) and (x % 42 == 0)) or (x % A == 0)) and (A * (A - 25) < 25 * (A + 200))):
            ok = False
            break

    if ok:
        print(A)