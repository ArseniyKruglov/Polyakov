file = open('24-j5.txt', 'r')
string = file.readline()
count = 0

for i in range (0, len(string)):
    if (string[i : i + 7] == 'SOCKCOS'):
        count += 1

print (count)
