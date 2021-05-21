for i in range(-1000, 1000):
    x = i
    a = 0
    b = 0
    
    while x > 0:
        a = a + 1
        if x % 2 == 0:
            b = b + (x % 10)
        x = x // 10

    if a == 3 and b == 18:
        print(i)
        break
