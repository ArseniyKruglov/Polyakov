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

##def f(x, y):
##    if y < x:
##        return 0
##    if y == x:
##        return 1
##    k = f(x, y - 1)
##    k+= f(x, y - 2)
##    if y % 3 == 0:
##        k+= f(x, y // 3)
##    return k
##print(f(1, 27))
