file = open('24-153.txt', 'r')
string = file.readline()

look = False
temp = ''
c = 0

for i in range(0, len(string)):
    if string[i] == 'A':
        look = True

    if look:
        temp += string[i]

    if string[i] == 'F':
        look = False
        if 7 <= len(temp) and len(temp) <= 10:
            c += 1
        temp = ''

print(c)
