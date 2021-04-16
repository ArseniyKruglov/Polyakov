for N in range(0, 1000):
    b = bin(N)[2:]
    if b[-1] == '0':
        b += '00'
    else:
        b += '11'

    if int(b, 2) > 115:
        print(N)
        break
