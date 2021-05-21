for i in range(12034679, 23175821 + 1):
    if i ** 0.25 % 1 == 0:
        dividers = []
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                dividers.append(j)
                dividers.append(i // j)
                
        dividers = list(set(dividers))
        dividers.sort()

        if len(dividers) == 3:
            print(i, dividers[-1])
