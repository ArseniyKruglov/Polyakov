def ToN(n, o):
    s = ''
    while n > 0:
        s = str(n % o) + s
        n //= o
    return s

for i in range(2, 10 + 1):
    print(ToN(1988, i), i)
