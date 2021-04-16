primes = []
for i in range(2, 55555 + 1):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        primes.append(i)

for i in range(33333, 55555 + 1):
    prime_dividers = []
    for prime in primes:
        if prime > int(i ** 0.5):
            break
        
        if i % prime == 0:
            prime_dividers.append(prime)

    sum = 0;
    for prime_divider in prime_dividers:
        sum += prime_divider;

    if sum > 250 and i % sum == 0:
        print(i, sum)