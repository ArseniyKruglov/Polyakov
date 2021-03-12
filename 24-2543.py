file = open('24-5.txt', 'r')
string = file.readline()
count = 0

for i in range (0, len(string)):
    if (string[i : i + 2] == '()'):
        count += 1

    if (count == 10000):
        print(i + 1)
        break
