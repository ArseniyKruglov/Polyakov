for i in range(11275, 16328 + 1):
    dividers = []
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            dividers.append(j)
            dividers.append(i // j)

    if len(set(dividers)) == 3:
        dividers = list(set(dividers))
        dividers.sort()
        print(dividers[-2], dividers[-1])
