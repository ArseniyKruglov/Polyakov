def F(n):
    if n <= 1:
        return 1
    else:
        if n % 2 == 0:
            return 3 + F(n/2 - 1)
        else:
            return n + F(n + 2)

for i in range(10000):    
    try:
        if F(i) == 19:
            print(i)
            break
    except:
        pass
