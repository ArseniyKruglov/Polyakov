a = []

for n in range (1, 10000):
    n = bin(n)
    n = n[2:]

    if n.count('1') > n.count('0'):
        n += '0'
    else:
        n += '1'

    if len(n) % 2 == 0:
        n = n[:3] + n [5:]
    else:
        n = n[:2] + n [5:]
    
    n = int(n, 2)

    if 50 <= n and n <= 100:
        a.append(n)

print(len(set(a)))
