file = open('24-1.txt', 'r')
string = file.readline()
length = 0
max = 0
result = 0

for i in range (0, len(string) - 1):
    if (ord(string[i]) > ord(string[i + 1])):
        length += 1
    else:
        length = 0

    if (length > max):
        max = length
        result = i - length + 1 + 1

print(result)
