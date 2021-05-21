file = open('27.txt', 'r')

n = int(file.readline())
data = []

for i in range(0, n):
    data.append(int(file.readline()))

answer = 100000

for i in range(0, n):
    answer = min(answer, data[i] ** 2 + min(data[0 : i - 6] + data[i + 6 : -1]) ** 2)

print(answer)
