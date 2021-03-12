def F(n, g):
    global c
    
    if n == g:
        c += 1

    if n < 12:
        F(n + 1, g)
        F(n + 2, g)
        F(n * 2, g)

c = 0
F(2, 10)

temp = c
c = 0
F(10, 12)

print(c * temp)
