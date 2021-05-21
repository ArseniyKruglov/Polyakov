def F(n, g):
    if n == g:
        global count
        count += 1

    if n < g:
        F(n + 1, g)
        F(n + 2, g)
        F(n * 3, g)

count = 0
F(2, 14)

temp = count
count = 0
F(14, 16)

print(count * temp)
