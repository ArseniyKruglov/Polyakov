def F(n, g):
    if n == g:
        global c
        c += 1

    if n < g:
        F(n + 1, g)
        F(n + 2, g)
        F(n * 2, g)

c = 0
F(1, 7)

t1 = c
c = 0
F(7, 10)

t2 = c
c = 0
F(10, 12)

print(t1 * t2 * c)
