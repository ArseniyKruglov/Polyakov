def F(n):
    if n <= 3:
        return n
    else:
        if n % 2 == 0:
            return n + F(n - 1)
        else:
            return n * n + F(n - 2)

count = 0
for i in range(1, 1000):
    if F(i) < 10 ** 8:
        count += 1
print(count)
