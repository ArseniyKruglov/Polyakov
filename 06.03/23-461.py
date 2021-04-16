def F(n, g):
    global count
    
    if n == g:
        count += 1

    if n < g and n != 10:
        F(n + 1, g)
        F(n * 2, g)

count = 0
F(3, 25)

temp = count
count = 0
F(25, 28)

print(temp * count)
