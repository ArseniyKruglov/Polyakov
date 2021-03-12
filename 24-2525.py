file = open('24-1.txt', 'r')
string = file.readline()
temp = ''
max = 0

for i in range (0, len(string)):
    if (string[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
        temp += string[i]
    else:
        if (temp != ''):
            temp = int(temp)
            if (temp % 2 == 0):
                if (temp > max):
                    max = temp

        temp = ''

print(max)
