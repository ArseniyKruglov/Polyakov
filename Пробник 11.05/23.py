def F(n):
    if n == 25:
        global c
        c += 1

    if n < 25:
        F(n + 1)
        F(n * 3)
        F(n * 4)

c = 0
F(1)
print(c)
