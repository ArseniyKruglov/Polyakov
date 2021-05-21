def F(n, g):
    if n == g:
        global c
        c += 1

    if n < g and n != 25:
        F(n + 1, g)
        F(n * 2, g)
        F(n * 3, g)

c = 0
F(3, 12)

t = c
c = 0
F(12, 46)

print(c * t)
