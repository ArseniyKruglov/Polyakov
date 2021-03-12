import math

n = 0

for i in range (1371085, 1371134):
    prime = True
    
    for j in range (2, int(math.sqrt(i)) + 1):
        if (i % j == 0):
            prime = False
            break

    if (prime):
        n += 1
        print(n, i)
        
