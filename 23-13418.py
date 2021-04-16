def F(n):
    if n == 27:
        global count
        count += 1

    if n < 27 and n != 26:
        F(n + 1)
        F(2 * n + 1)

count = 0
F(1)
print(count)