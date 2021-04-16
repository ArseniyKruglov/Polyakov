def F(n, g):
    global count
    
    if n == g:
        count += 1

    if n < 12:
        F(n + 1, g)
        F(n + 2, g)
        F(n * 2, g)

count = 0
F(2, 10)

temp = count
count = 0
F(10, 12)

print(count * temp)
