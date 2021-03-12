import math

for i in range (126849, 126871 + 1):
    dividers = []
    dividers.append(1)
    dividers.append(i)
    
    for j in range (2, int(math.sqrt(i)) + 1):
        if (i % j == 0):
            dividers.append(j)
            dividers.append(i // j)

    if (len(dividers) == 4):
        dividers.sort()
        print(dividers[2], dividers[3])
