# Текстовый файл k8-10.txt состоит не более чем из 106 символов. Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.

file = open('Source/24-1.txt', 'r')
temp = ''
max = 0

for char in file.readline():
    if temp != '':
        print(temp)
        
    if char in '0123456789':
        temp += char
    else:
        if (temp != ''):
            temp = int(temp)
            if temp % 2 == 0 and temp > max:
                max = temp

        temp = ''

print(max)
