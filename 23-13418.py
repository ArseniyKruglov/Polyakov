def F(n):
    global c
    if n == 27:
        c += 1

    if n < 27 and n != 26:
        F(n + 1)
        F(2 * n + 1)

c = 0
F(1)
print(c)
