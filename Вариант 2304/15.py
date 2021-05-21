for A in range(-1000, 1000):
    ok = True

    for x in range(0, 1000):
        for y in range(0, 1000):
            if not( (3 * x + 4 * y != 48) or ((A > x) and (A > y)) ):
                ok = False
                break

        if not ok:
            break

    if ok:
        print(A)
        break
