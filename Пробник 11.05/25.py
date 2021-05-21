for i in range(135743, 135789 + 1):
    dividers = [1, i]
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            dividers.append(j)
            dividers.append(i // j)

    if len(dividers) == 6:
        dividers.sort()
        print(dividers[-2], dividers[-1])
