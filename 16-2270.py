def F(n):
    if n <= 3:
        return n
    else:
        if n % 2 == 0:
            return n + F(n - 1)
        else:
            return n * n + F(n - 2)

c = 0
for i in range(1, 1000):
    if F(i) < 10 ** 8:
        c += 1
print(c)
