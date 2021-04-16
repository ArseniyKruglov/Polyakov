primes = []
for i in range(2, int((107000000 / 2) ** 0.5) + 1):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        primes.append(i)

for i in range(106000000, 107000000 + 1):
    if (i / 2) ** 0.5 in primes:
        print(i)
