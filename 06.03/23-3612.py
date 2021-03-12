def F(n, g):
    global c
    
    if n == g:
        c += 1

    if n < g:
        F(n + 2, g)
        F(n + 3, g)
        F(int(str(n) + '1'), g)

c = 0
F(3, 12)

temp = c
c = 0
F(12, 25)

print(c * temp)


