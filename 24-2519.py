# В текстовом файле k7a-5.txt находится цепочка из символов латинского алфавита A, B, C, D, E, F. Найдите длину самой длинной подцепочки, не содержащей символов C и F.

file = open('Source/k7a-5.txt', 'r')
length = 0
max = 0

for char in file.readline():
    if (char != 'C' and char != 'F'):
        length += 1
    else:
        length = 0

    if (length > max):
        max = length

print(max)
