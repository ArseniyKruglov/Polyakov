def F(n, g):
    global c
    
    if n == g:
        c += 1

    if n < g and n != 10:
        F(n + 1, g)
        F(n * 2, g)

c = 0
F(3, 25)

temp = c
c = 0
F(25, 28)

print(temp * c)
