# Рассматриваются целые числа, принадлежащих числовому отрезку [278932; 325396], которые представляют собой произведение трёх различных простых делителей, оканчивающихся на одну и ту же цифру. В ответе запишите количество таких чисел и максимальное из них.

primes = []
for i in range(2, 325396 + 1):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        primes.append(i)

max = 0
c = 0

for i in range(278932, 325396 + 1):
    ok = False
    
    dividers = []
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            dividers.append(j)
            dividers.append(i // j)

    if len(dividers) == 6:
        prime_dividers = []
        for divider in dividers:
            if divider in primes:
                prime_dividers.append(divider)

        for prime_divider_1 in prime_dividers:
            for prime_divider_2 in prime_dividers:
                for prime_divider_3 in prime_dividers:
                    if prime_divider_1 != prime_divider_2 != prime_divider_3 and prime_divider_1 % 10 == prime_divider_2 % 10 == prime_divider_3 % 10 and prime_divider_1 * prime_divider_2 * prime_divider_3 == i:
                        ok = True
                        break
                if ok:
                    break
            if ok:
                break

        if ok:
            c += 1
            max = i

print(c, max)
