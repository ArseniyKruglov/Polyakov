for A in range(0, 1000):
    ok = True

    for x in range(1, 1000):
        for y in range(1, 1000):
            if not((5 * y + 7 * x != 129) or (3 * x > A) or (4 * y > A)):
                ok = False
                break

        if not ok:
            break

    if ok:
        print(A)
