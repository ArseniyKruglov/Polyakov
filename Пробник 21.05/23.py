def F(n):
    if n == 2:
        global c
        c += 1

    if n > 2:
        F(n - 2)
        F(n - 5)

c = 0
F(23)
print(c)
