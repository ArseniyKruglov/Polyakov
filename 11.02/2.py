primes = []
for i in range(2, int((345293 + 1) ** 0.5) + 1):
    prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            prime = False
            break

    if prime:
        primes.append(i)

c = 0

for i in range(158928, 345293 + 1):
    dividers = []
    dividers.append(1)
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            dividers.append(j)
            dividers.append(i // j)
    dividers.append(i)

    if len(dividers) == 8:
        c += 1

print(c)
    
