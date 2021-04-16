n = 95
n = bin(n)
n = '0' + n[2:]
n = n.replace('0', '2').replace('1', '0').replace('2', '1')
n = int(n, 2)
n += 1

print(n)