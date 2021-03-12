def F(n, g):
    global c
    if n == g:
        c += 1

    if n < g and n != 10 and n != 11:
        F(n + 1, g)
        F(n + 2, g)
        F(n * 3, g)

c = 0
F(1, 8)

temp = c
c = 0
F(8, 27)

print(temp * c)
