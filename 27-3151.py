file = open('27-3151.txt','r')

n = int(file.readline())
sum1 = 0
sum2 = 0
sum3 = 0

for i in range(0, n):
    c1 , c2 , c3 = list(map(int ,file.readline().strip().split(' ')))

    if c1 > c2 > c3:
        sum1 += c1
        sum2 += c2
        sum3 += c3
    if c2 > c1 > c3:
        sum1 += c2
        sum2 += c1
        sum3 += c3
    if c3 > c1 > c2:
        sum1 += c3
        sum2 += c1
        sum3 += c2
    if c3 > c2 > c1:
        sum1 += c3
        sum2 += c2
        sum3 += c1
    if c2 > c3 > c1:
        sum1 += c2
        sum2 += c3
        sum3 += c1
    if c1 > c3 > c2:
        sum1 += c1
        sum2 += c3
        sum3 += c2

if (sum1 % 2 == 1) and (sum2 % 2 == 1):
    print(sum3)
else:
    if (sum1 % 2 == 0) and (sum2 % 2 == 0):
        file = open('count:\\PABCWork.NET\\Py\\files\\27-45b.txt','r')
        min2 = 10000
        min = 10000
        n = int(file.readline())

        for i in range(0, n):
            c1 , c2 , c3 = list(map(int ,file.readline().strip().split(' ')))
        
            if abs(c1 - c2) < abs(c2 - c3) < abs(c1 - c3) and min > abs(c1 - c2) and abs(c1 - c2) % 2 == 1:
                min2 = min
                min = abs(c1 - c2)
                
            if abs(c2 - c3) < abs(c1 - c2) < abs(c1 - c3) and min > abs(c2 - c3) and abs(c2 - c3) % 2 == 1:
                min2 = min
                min = abs(c2 - c3)

            if abs(c1 - c3) < abs(c2 - c3) < abs(c1 - c2) and min > abs(c1 - c3) and abs(c1 - c3) % 2 == 1:
                min2 = min
                min = abs(c1 - c3)

        file = open('count:\\PABCWork.NET\\Py\\files\\27-45b.txt','r')
        min3 = min2
        n = int(file.readline())

        for i in range(n, 0, -1):
            c1 , c2 , c3 = list(map(int ,file.readline().strip().split(' ')))
        
            if abs(c1 - c2) < abs(c2 - c3) < abs(c1 - c3) and min < abs(c1 - c2) < min2 and abs(c1 - c2) % 2 == 1 and min3 > abs(c1 - c2):
                min3 = abs(c1 - c2)
                
            if abs(c2 - c3) < abs(c1 - c2) < abs(c1 - c3) and min < abs(c2 - c3) < min2 and abs(c2 - c3) % 2 == 1 and min3 > abs(c2 - c3):
                min3 = abs(c2 - c3)

            if abs(c1 - c3) < abs(c2 - c3) < abs(c1 - c2) and min < abs(c1 - c3) < min2 and abs(c1 - c3) % 2 == 1 and min3 > abs(c1 - c3):
                min3 = abs(c1 - c3)

        if min2 == min3:
            print(sum3 + min + min2)
        else:
            print(sum3 + min + min3)
 
        
    if (sum1 % 2 == 0) and (sum2 % 2 == 1):
        file = open('count:\\PABCWork.NET\\Py\\files\\27-45b.txt','r')
        min2 = 10000
        min = 10000
        n = int(file.readline())

        for i in range(0, n):
            c1 , c2 , c3 = list(map(int ,file.readline().strip().split(' ')))

            if abs(c1 - c2) < abs(c2 - c3) < abs(c1 - c3) and min > abs(c1 - c2) and abs(c1 - c2) % 2 == 1:
                min = abs(c1 - c2)
                
            if abs(c2 - c3) < abs(c1 - c2) < abs(c1 - c3) and min > abs(c2 - c3) and abs(c2 - c3) % 2 == 1:
                min = abs(c2 - c3)

            if abs(c1 - c3) < abs(c2 - c3) < abs(c1 - c2) and min > abs(c1 - c3) and abs(c1 - c3) % 2 == 1:
                min = abs(c1 - c3)
        print(sum3 + min)
        
    if (sum2 % 2 == 0) and (sum1 % 2 == 1):
        file = open('count:\\PABCWork.NET\\Py\\files\\27-45b.txt','r')
        min2 = 10000
        min = 10000
        n = int(file.readline())

        for i in range(0, n):
            c1 , c2 , c3 = list(map(int ,file.readline().strip().split(' ')))

            if abs(c1 - c2) < abs(c2 - c3) < abs(c1 - c3) and min > abs(c1 - c2) and abs(c1 - c2) % 2 == 1:
                min = abs(c1 - c2)
                
            if abs(c2 - c3) < abs(c1 - c2) < abs(c1 - c3) and min > abs(c2 - c3) and abs(c2 - c3) % 2 == 1:
                min = abs(c2 - c3)

            if abs(c1 - c3) < abs(c2 - c3) < abs(c1 - c2) and min > abs(c1 - c3) and abs(c1 - c3) % 2 == 1:
                min = abs(c1 - c3)
        print(sum3 + min)