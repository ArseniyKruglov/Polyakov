file = open('k7a-5.txt', 'r')
string = file.readline()
length = 0
max = 0

for i in range (0, len(string) - 1):
    if (string[i] != 'C' and string[i] != 'F'):
        length += 1
    else:
        length = 0

    if (length > max):
        max = length

print(max)
