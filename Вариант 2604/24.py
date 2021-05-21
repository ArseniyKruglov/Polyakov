file = open('24.txt', 'r')
string = file.readline()

for i in range(0, 1000):
    if '(' * i in string:
        print(i)
