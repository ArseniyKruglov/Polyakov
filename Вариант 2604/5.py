N = 120

N = bin(N)[2:]
N = (8 - len(N)) * '0' + N
N = N.replace('0', '2').replace('1', '0').replace('2', '1')

print(int(N, 2) + 1)
