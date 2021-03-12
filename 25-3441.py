import math

primes = []
for i in range(2, 55555 + 1):
    ok = True
    
    for j in range(2, i):
        if (i % j == 0):
            ok = False
            break
        
    if (ok):
        primes.append(i)

for i in range(33333, 55555 + 1):
    local = []
    for prime in primes:
        if (i % prime == 0 and prime != i):
            local.append(prime)

    sum = 0;
    for element in local:
        sum += element;

    if (sum > 250 and i % sum == 0):
        print(i, sum)
