file = open('Source/24-1.txt', 'r')
temp = ''
max = 0

for char in file.readline():
    if (char in '0123456789'):
        temp += char
    else:
        if (temp != ''):
            temp = int(temp)
            if (temp % 2 == 0):
                if (temp > max):
                    max = temp

        temp = ''

print(max)
