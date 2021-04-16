for i in range (854321, 1087654 + 1):
    dividers = []
    for j in range (2, int(i ** 0.5) + 1):
        if (i % j == 0):
            dividers.append(j)
            dividers.append(i // j)

    if (len(dividers) >= 2):
        ok = True

        for j in range (0, len(dividers) - 1):
            if (dividers[j + 1] - dividers[j] != 10):
                ok = False
                break

        if (ok):
            print(i, dividers[0])
