for A in range(1, 1000):
    ok = True

    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(((y >= -4 * x + 12) and (y >= 4 * x - 12)) == (y >= A * abs(x - 3))):
                ok = False
                break

        if not ok:
            break

    if ok:
        print(A)