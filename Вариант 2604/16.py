def F(n):
    if n > 25:
        return 2*n*n*n + 1
    else:
        return F(n+2) + 2*F(n+3)

count = 0

for i in range(1, 1000 + 1):
    if F(i) % 11 == 0:
        count += 1

print(count)
