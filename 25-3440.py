for i in range (33333, 55555 + 1):
    prime = True
    for j in range (2, i):
        if (i % j == 0):
            prime = False
            break

    if (prime):
        sum = 0;
        prime = i
        
        while (prime > 0):
            sum += prime % 10
            prime = prime // 10

        if (sum > 35):
            print(i, sum)