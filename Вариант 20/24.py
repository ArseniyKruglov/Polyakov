file = open('24.txt', 'r')
string = file.readline()

for i in range(1, 100000):
    if '(' * i in string:
        print(i)
