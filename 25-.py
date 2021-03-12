import math

primes = []
for i in range (2, int(math.sqrt(220784)) + 1):
    prime = True
    
    for j in range (2, int(math.sqrt(i)) + 1):
        if (i % j == 0):
            prime = False
            break

    if (prime):
        primes.append(i)

primes.sort(reverse = True)
array = []

for i in range (105673, 220784 + 1):
    prime_dividers = []
    n = i

    for prime in primes:
        if (i % prime == 0):
            prime_dividers.append(prime)
            i //= prime

    if len(prime_dividers) == 3:
        if prime_dividers[0] * prime_dividers[1] * prime_dividers[2] == n:
            array.append(n)

array.sort()
print(len(array), array[-1])
