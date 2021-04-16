primes = []
for i in range(2, 529678 + 1):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        primes.append(i)

count = 0
min = 1000000

for i in range(485617, 529678 + 1):
    dividers = []
    for j in range (2, int(i ** 0.5) + 1):
        if i % j == 0:
            dividers.append(j)
            dividers.append(i // j)

    if len(dividers) == 6:
        prime_dividers = []
        for divider in dividers:
            if divider in primes:
                prime_dividers.append(divider)
                
        found = False
        for prime_divider_1 in prime_dividers:
            for prime_divider_2 in prime_dividers:
                for prime_divider_3 in prime_dividers:
                    if prime_divider_1 != prime_divider_2 != prime_divider_3 and prime_divider_1 * prime_divider_2 * prime_divider_3 == i and prime_divider_1 % 10 == prime_divider_2 % 10 == prime_divider_3 % 10:
                        count += 1

                        the_prime_dividers = [prime_divider_1, prime_divider_2, prime_divider_3]
                        the_prime_dividers.sort()
                        if (the_prime_dividers[2] - the_prime_dividers[0] < min):
                            min = the_prime_dividers[2] - the_prime_dividers[0]
                            min_i = i

                        found = True
                        break
                if found:
                    break
            if found:
                break

print(count, min_i)
