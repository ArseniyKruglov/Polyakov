def F(n):
    if n <= 3:
        return n
    else:
        if n % 2 == 0:
            return F(n - 1) + 2 * F(n / 2)
        else:
            return F(n - 1) + F(n - 3)
        
c = 0
        
for i in range(1, 100000):
    if F(i) < 10 ** 8:
        c += 1
        print(c)

print(c)
