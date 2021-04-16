file = open('24-2519.txt', 'r')

length = 0
answer = 0

for char in file.readline():
    if (char != 'C' and char != 'F'):
        length += 1
    else:
        length = 0

    answer = max(answer, length)

print(answer)