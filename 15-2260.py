for A in range (1, 1000):
    for x in range (1, 1000):
        if not(not((x % A == 0) and (x % 24 == 0) and not(x % 16 == 0)) or not(x % A == 0)):
            break
    else:
        print(A)
        break