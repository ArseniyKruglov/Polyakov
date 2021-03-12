def G(n):
    global c
    if n == 14:
        c += 1

    if n < 14 and n != 5 and n != 10:
        G(n + 1)
        G(n * 2)
        G(n + 3)

c = 0
G(2)
print(c)
