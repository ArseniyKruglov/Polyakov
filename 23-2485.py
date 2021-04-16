def F(n):
    if n == 55:
        global c
        c += 1

    if n < 55:
        F(n + 1)
        F(n * 4)

c = 0
F(1)
print(c)
