def F(n):
    if n > 25:
        return n*n + 2*n + 1
    else:
        if n % 2 == 0:
            return 2*F(n+1) + F(n+3)
        else:
            return F(n+2) + 3*F(n+5)

c = 0

for i in range(1, 1000 + 1):
    if '0' not in str(F(i)):
        c += 1

print(c)
