file = open('24-2522.txt', 'r')
string = file.readline()

length = 1
answer = 0

for i in range (0, len(string) - 1):
    if (string[i] != string[i + 1]):
        length += 1
    else:
        length = 1

    answer = max(answer, length)

print(answer)