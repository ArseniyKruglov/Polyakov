def F(n, g):
    if n == g:
        global c
        c += 1

    if n < g and n != 25:
        F(n + 1, g)
        F(n * 2, g)

c = 0
F(2, 14)

temp = c
c = 0
F(14, 29)

print(temp * c)
