def F(n, g):
    if n == g:
        global count
        count += 1

    if n < g and n != 25:
        F(n + 1, g)
        F(n * 2, g)

count = 0
F(2, 14)

temp = count
count = 0
F(14, 29)

print(temp * count)
