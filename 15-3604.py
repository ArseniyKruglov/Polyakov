for A in range(0, 1000):
    ok = True

    for x in range(0, 1000):
        for y in range(0, 1000):
            if not((5 * x - 6 * y < A) or (x - y > 30)):
                ok = False
                break

        if not ok:
            break

    if ok:
        print(A)
        break