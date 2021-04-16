file = open('27-21b.txt', 'r')

a = []
mn = 1000000

for i in range(0, int(file.readline())):
    a.append(list(map(int, file.readline().replace('\n', '').replace('  ', ' ').split(' '))))

s = 0
r = 0

for i in range(0, 2 ** 20):
    b = bin(i)[2:]
    b = (20 - len(b)) * '0' + b

    s = 0
    
    for j in range(0, 20):
        s += a[s[i]]

    

print(s - mn)
