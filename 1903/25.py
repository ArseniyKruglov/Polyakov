import math

for i in range(652938, 1744328 + 1):
    dividers = []
    for j in range(2,int(math.sqrt(i)) + 1):
        if i % j == 0:
            dividers.append(j)
            dividers.append(i // j)

    if len(dividers) == 3:
        dividers.sort()
        print(dividers[-2], dividers[-1])
