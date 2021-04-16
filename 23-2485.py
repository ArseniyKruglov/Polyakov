def F(n):
    if n == 55:
        global count
        count += 1

    if n < 55:
        F(n + 1)
        F(n * 4)

count = 0
F(1)
print(count)
