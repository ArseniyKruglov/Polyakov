def F(n, g):
    if n == g:
        global count
        count += 1

    if n < g:
        F(n + 2, g)
        F(n + 3, g)
        F(n * 10 + 1, g)

count = 0
F(3, 12)

temp = count
count = 0
F(12, 25)

print(temp * count)