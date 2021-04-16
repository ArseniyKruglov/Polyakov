file = open('24-5.txt', 'r')
string = file.readline()

c = 0

for i in range(0, len(string)):
    if string[i] == '(':
        c += 1

    if c == 10000:
        print(i + 1)
        break
