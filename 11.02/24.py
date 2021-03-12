file = open('24.txt', 'r')
string = file.readline()

length = 0
max = 0
a = ''

for i in range(0, len(string) - 1):
    if ord(string[i]) > ord(string[i + 1]):
        length += 1
    else:
        length += 1

        if length > max:
            max = length
            a = string[(i - length + 1) : i + 1]

        length = 0

print(a, max)


