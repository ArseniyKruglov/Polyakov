file = open('24.txt', 'r')
string = file.readline()

answer = 0

for i in range(0, 10000):
    if 'C' * i in string:
        answer = i

print(answer)
