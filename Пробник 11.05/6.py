for i in range(100000):
    s = 535
    n = 5
    while n > 0:
        s = s + n
        n = n - 1
    if s <= 550:
        print(s)
