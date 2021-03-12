array = []
for n in range (1, 100000):
    new_n = ''
    while n > 0:
        new_n = str(n % 6) + new_n
        n //= 6

    new_n += new_n[-1]

    new_n = int(new_n, 6)
    new_n = bin(new_n)
    new_n = str(new_n)
    new_n += new_n[-1]

    array.append(int(new_n, 2))

array.sort()

for i in range (0, len(array)):
    if (array[i] == 344):
        print(array[i - 1])
        break
