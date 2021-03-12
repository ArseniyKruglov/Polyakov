primes = []
for i in range(2, 315675 + 1):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        primes.append(i)

c = 0
max_i = 0
max_difference = 0

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
                break
        if ok:
            break
    if ok:
        c += 1
        if abs(prime_dividers[1] - prime_dividers[0]) > max_difference:
            max_difference = abs(prime_dividers[1] - prime_dividers[0])
            max_i = i

print(c, max_i)
    
            
    
