for N in range(0, 100000):
    N = bin(N)[2:]
    N += str(N.count('1') % 2)
    N += str(N.count('1') % 2)

    if int(N, 2) > 396:
        print(int(N, 2))
        break
