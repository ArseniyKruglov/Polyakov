for i in range(1000 + 1, 10000):
    binary = bin(i)[2:]
    binary = binary[::-1]

    if int(binary, 2) == 29:
        print(i)
        break