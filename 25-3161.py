import math

for i in range (2000000, 3000000 + 1):
    pairs = []
    for j in range (2, int(math.sqrt(i)) + 1):
        if (i % j) == 0:
            pairs.append([j, i // j])

    count = 0
    max = 0
    for pair in pairs:
        if (pair[1] - pair[0] <= 120):
            count += 1
            
            if (pair[1] > max):
                max = pair[1]

    if (count >= 3):
        print(i, max)
