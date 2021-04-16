def F(n):
    global count
    
    if n == 63:
        count += 1

    if n < 63 and n != 43:
        F(n + 2)
        F(n + n - 1)
        F(n + n + 1)

count = 0
F(7)

print(count)
