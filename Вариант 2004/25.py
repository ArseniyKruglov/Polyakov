for i in range(194455, 194500 + 1):
    dividers = []
    dividers.append(1)
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            dividers.append(j)
            dividers.append(i // j)
    dividers.append(i)

    dividers = sorted(list(set(dividers)))

    if len(dividers) == 4:
        print(dividers[-2], dividers[-1])
