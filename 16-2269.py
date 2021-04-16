def F(n):
    if n <= 3:
        return n
    else:
        if n % 2 == 0:
            return F(n - 1) + 2 * F(n / 2)
        else:
            return F(n - 1) + F(n - 3)
        
count = 0
        
for i in range(1, 100000):
    if F(i) < 10 ** 8:
        count += 1
        print(count)

print(count)
