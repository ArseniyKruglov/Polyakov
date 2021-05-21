c = 0

for i in range (452021 + 1, 10000000):
    dividers = []
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            dividers.append(j)
            dividers.append(i // j)
    dividers = set(dividers)

    if len(dividers) > 1:
        M = min(dividers) + max(dividers);
        if M % 7 == 3:
            c += 1
            print(i, M)

            if c == 5:
                break

