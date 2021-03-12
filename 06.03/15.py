for A in range(1, 1000):
    ok = True

    for X in range(1, 1000):
        if not((not((X & 13 != 0) or (X & A == 0)) or (X & 13 != 0)) or (X & A != 0) or (X & 39 == 0)):
            ok = False
            break

    if ok:
        print(A)
        break
