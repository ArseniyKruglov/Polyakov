def F(n):
    global count
    if n == 19:
        count += 1

    if n < 19:
        F(n + 1)
        F(n + 3)
        F(n ** 2)

count = 0
F(2)
print(count)
