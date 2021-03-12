# Текстовый файл 24-j9.txt состоит не более чем из 106 символов английского алфавита. Определите количество палиндромов (последовательностей, которые читаются в обе стороны одинаково) длиной 5 символов.

file = open('Source/24-j9.txt', 'r')
string = file.readline()
count = 0

for i in range (0, len(string)):
    if string[i : i + 5 : 1] == string[i + 4 : i - 1 : -1]:
        count += 1

print(count)
