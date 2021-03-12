file = open('27-47a.txt', 'r')

min_n = 10000
min = 0
max = 0

n = int(file.readline())

for i in range(0, n):
    c1, c2 = list(map(int, file.readline().strip().split(' ')))

    if c1 > c2:
        max += c1
        min += c2
    else:
        max += c2
        min += c1

if min % 10 != max % 10:
    file = open('27-47a.txt', 'r')
    file.readline()

    for i in range(0, n):
        c1, c2 = list(map(int, file.readline().strip().split(' ')))
        
        if (abs(c1 - c2) % 10 == abs(max % 10 - min % 10)) and (abs(c1 - c2) < min_n):
            min_n = abs(c1 - c2)

    print(min + min_n)
else:
    print(min)
