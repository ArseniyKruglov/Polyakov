count = 0

for n in range (2, 10000):
    n = bin(n)
    n = n[2:]
    n += n[-2]
    n += n[1]
    n = int(n, 2)

    if 150 <= n and n <= 200:
        count += 1
        
print(count)
