file = open('27B.txt', 'r')

n = int(file.readline())
array = []
for i in range(0, n):
    array.append(list(map(int, (file.readline().strip('\n').split(' ')))))

answer = 0
diff = []

for pair in array:
    answer += min(pair)

for pair in array:
    diff.append(abs(pair[0] - pair[1]))

done = False

for i in range(0, 10000):
    for pair in array:
        if (answer + i) % 10 == 4:
            print(i)
            done = True
            break

    if done:
        break
