file = open('Source/24-2525txt', 'r')

temp = ''
answer = 0

for char in file.readline():
    if temp != '':
        print(temp)
        
    if char in '0123456789':
        temp += char
    else:
        if (temp != ''):
            temp = int(temp)
            if temp % 2 == 0:
                answer = max(answer, temp)

        temp = ''

print(answer)