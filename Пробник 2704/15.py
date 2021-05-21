for A in range(1, 10000):
    ok = True

    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(((y <= 5*x - 14) and (y <= -5*x + A)) == (y-6 <= -5*abs(x - 4))):
                ok = False
                break

        if not ok:
            break

    if ok:
        print(A)
