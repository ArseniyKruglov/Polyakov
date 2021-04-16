def G(n):
    if n == 14:
        global count
        count += 1

    if n < 14 and n != 5 and n != 10:
        G(n + 1)
        G(n * 2)
        G(n + 3)

count = 0
G(2)
print(count)