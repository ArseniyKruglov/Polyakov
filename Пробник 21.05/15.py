P1 = 17
P2 = 54

Q1 = 37
Q2 = 83

min_ = 1000000

for A1 in range(-100, 100):
    for A2 in range(100, -100, -1):
        ok = True

        for x in range(-1000, 1000):
            if not(   (P1 <= x <= P2) <= (((Q1 <= x <= Q2) and (not(A1 <= x <= A2))) <= (not(P1 <= x <= P2)))   ):
                ok = False
                break

        if ok:
            min_ = min(min_, abs(A2 - A1))

print(min_)
