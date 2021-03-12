file = open('Source/24-153.txt', 'r')

look = False
temp = ''
c = 0

for char in file.readline():
    if char == 'A':
        look = True

    if look:
        temp += char

    if char == 'F':
        look = False
        if 7 <= len(temp) and len(temp) <= 10:
            c += 1
        temp = ''

print(c)

# Ответ не совпадает
