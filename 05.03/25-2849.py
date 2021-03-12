primes = []
for i in range(2, int(345293 ** 0.5) + 1):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        primes.append(i)

c = 0
for i in range(158928, 345293 + 1):
    a = 0
    dividers = []

    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            dividers.append(j)
            dividers.append(i // j)

    if len(dividers) == 6:
        for divider in dividers:
            if a > 3:
                break
            
            if divider in primes:
                a += 1

        if a == 3:
            c += 1
            if c == 1:
                print(i)

print(c)



