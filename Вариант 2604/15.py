for A in range(-1000, 1000):
    ok = True

    for x in range(1, 1000):
        for y in range(1, 1000):
            if not( (-y + 2*x < A) or (x > 15) or (y > 28) ):
                ok = False
                break

        if not ok:
            break

    if ok:
        print(A)
        break
