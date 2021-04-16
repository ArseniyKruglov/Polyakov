for A in range(1, 1000):
    ok = True

    for x in range(1, 1000):
        for y in range(1, 1000):
            if not((3 * y - 4 * x - 29 != 0) or (A < 2 * x * x + 5) or (A < y * y - 1)):
                ok = False
                break

        if not ok:
            break

    if ok:
        print(A)