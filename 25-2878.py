array = []

for i in range (33333, 55555 + 1):
    i = str(i)
    if (int(i[0]) % 2 == 1 and int(i[1]) % 2 == 1 and int(i[2]) % 2 == 0 and int(i[3]) % 2 == 1 and int(i[4]) % 2 == 0 and int(i) % 6 != 0 and int(i) % 7 != 0 and int(i) % 8 != 0):
        array.append(int(i))

array.sort()
print(len(array), array[-1] - array[0])
