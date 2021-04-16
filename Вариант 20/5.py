for i in range(1000 + 1, 10000):
    b = bin(i)[2:]
    b = b[::-1]

    if int(b, 2) == 29:
        print(i)
        break
