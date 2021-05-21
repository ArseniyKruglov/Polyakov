c = 0
for i in range(0, 1000000):
    if i % 10 == 8:
        d = i
        S = 5
        N = 7
        while S <= 3011:
            S = S + d
            N = N + 124
        if N == 1247:
            c += 1
            print(c)
print(c)
