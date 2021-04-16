def F(n, g):
    if n == g:
        global count
        count += 1

    if n < g and n != 10 and n != 11:
        F(n + 1, g)
        F(n + 2, g)
        F(n * 3, g)

count = 0
F(1, 8)

temp = count
count = 0
F(8, 27)

print(temp * count)