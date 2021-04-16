def F(n, g):
    if n == g:
        global c
        c += 1

    if n < g:
        F(n + 1, g)
        F(n + 3, g)

c = 0
F(1, 15)
print(c)
