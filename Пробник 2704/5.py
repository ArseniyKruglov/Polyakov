def F(n):
    return n % 4 * 100 + n % 2 * 10 + n % 3

for i in range(10, 100):
    if F(i) == 112:
        print(i)
        break
