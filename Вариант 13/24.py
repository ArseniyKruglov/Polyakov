file = open('24-j5.txt', 'r')
string = file.readline()

for i in range(0, 10000):
    if string.count('KOT' * i) > 0:
        print(i)
