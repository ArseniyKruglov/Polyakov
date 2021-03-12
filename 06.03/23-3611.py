def F(n):
    global c
    
    if n == 63:
        c += 1

    if n < 63 and n != 43:
        F(n + 2)
        F(n + n - 1)
        F(n + n + 1)

c = 0
F(7)

print(c)
