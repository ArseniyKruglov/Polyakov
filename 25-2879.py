primes = []
for i in range(2532000, 2532160 + 1):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        primes.append(i)

for i in range(1, len(primes) + 1, 3):
    print(i, primes[i - 1])