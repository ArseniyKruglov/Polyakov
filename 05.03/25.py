primes = []
for i in range(2, int(315675 ** 0.5) + 1):
    prime = True
    
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            prime = False
            
    if prime:
        primes.append(i)

c = 0
max = [0, [0, 0]]

for i in range(238941, 315675 + 1):
    dividers = []
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            dividers.append(j)
            dividers.append(i // j)

    prime_dividers = []
    for divider in dividers:
        if divider in primes:
            prime_dividers.append(divider)

    ok = False

    for prime_divider_1 in prime_dividers:
        for prime_divider_2 in prime_dividers:
            if prime_divider_1 != prime_divider_2 and prime_divider_1 * prime_divider_2 == i:
                ok = True

    if ok:
        c += 1

        if prime_dividers[1] - prime_dividers[0] > max[0]:
            max = [prime_dividers[1] - prime_dividers[0], prime_dividers]

print(c, max[1])
    
            
    
