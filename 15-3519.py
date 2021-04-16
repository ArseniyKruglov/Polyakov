for A in range(1, 1000):
    for X in range(1, 1000):
        if not((not((X & 13 != 0) or (X & A == 0)) or (X & 13 != 0)) or (X & A != 0) or (X & 39 == 0)):
            break
    else:
        print(A)
        break