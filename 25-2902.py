import math

primes = []

for i in range (2532000, 2532160):
    prime = True
    
    for j in range (2, int(math.sqrt(i)) + 1):
        if (i % j == 0):
            prime = False
            break

    if (prime):
        primes.append(i)

primes.sort()

i = 0
for prime in primes:
    i += 1

    if (i - 1) % 3 == 0:
        print(i, prime)
