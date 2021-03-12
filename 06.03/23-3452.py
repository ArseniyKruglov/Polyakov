def F(n, l):
    global a
    a.append(n)
    
    if n < l:
        F(n + 2, l)
        F(n + 4, l)
        F(n + 5, l)

for l in range(1, 1000):
    a = []
    F(31, l)
    for n in set(a):
        if a.count(n) == 1001:
            print(n)
            break


