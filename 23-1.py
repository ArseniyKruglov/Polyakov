def F(n):
    global c
    if n == 19:
        c += 1

    if n < 19:
        F(n + 1)
        F(n + 3)
        F(n ** 2)

c = 0
F(2)
print(c)
