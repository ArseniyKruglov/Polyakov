for A in range(0, 1000):
    ok = True

    for x in range(0, 1000):
        for y in range(0, 1000):
            if not((75 != 2 * x + 3 * y) or (A > 3 * x) or (A > 2 * y)):
                ok = False
                break

        if not ok:
            break

    if ok:
        print(A)
        break