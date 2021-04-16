for i in range(-1000, 1000):
    x = i
    a = 1 
    b = 0
    while x > 0: 
        count = x % 10
        a = a*count
        if count > b: b = count
        x = x // 10

    if a == 48 and b == 6:
        print(i)
