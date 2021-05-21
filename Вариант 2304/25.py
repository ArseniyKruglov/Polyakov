for i in range(174457, 174505 + 1):
    dividers = []
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            dividers.append(j)
            dividers.append(i // j)

    if len(dividers) == 2:
        dividers.sort()
        print(dividers[-2], dividers[-1])
    
