def F(n):
    if n == int('11101', 2):
        global c
        c += 1

    if n < int('11101', 2):
        F(n + 1)
        F(int(bin(n)[2:] + '0', 2))
        F(int(bin(n)[2:] + '1', 2))

c = 0
F(int('100', 2))
print(c)
