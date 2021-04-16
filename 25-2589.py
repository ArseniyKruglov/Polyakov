for i in range(2, 30000 + 1):    
    dividers = [1]
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            dividers.append(j)
            dividers.append(i // j)

    dividers_2 = [1]
    for j in range(2, int(sum(dividers) ** 0.5) + 1):
        if sum(dividers) % j == 0:
            dividers_2.append(j)
            dividers_2.append(sum(dividers) // j)

    if i == sum(dividers_2) and sum(dividers) > i:
        print(i, sum(dividers))
