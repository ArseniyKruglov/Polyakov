for i in range (126849, 126871 + 1):
    dividers = []
    dividers.append(1)
    for j in range (2, int(i ** 0.5) + 1):
        if i % j == 0:
            dividers.append(j)
            dividers.append(i // j)
    dividers.append(i)

    if len(dividers) == 4:
        dividers.sort()
        print(dividers[2], dividers[3])
