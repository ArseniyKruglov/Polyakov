# Текстовый файл k8-10.txt состоит не более чем из 106 символов. Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.

file = open('Source/k8-10.txt', 'r')
string = file.readline()
length = 1
max = 0

for i in range (0, len(string) - 1):
    if (string[i] != string[i + 1]):
        length += 1
    else:
        length = 1

    if (length > max):
        max = length

print(max)
