file = open('27-3702.txt', 'r')

min = 0
even = 0
odd = 0

for i in range(0, int(file.readline())):
    c1, c2 = list(map(int, file.readline().strip().split(' ')))

    if c1 > c2:
        min += c2
        if c2 % 2 == 0:
            even += 1
        else:
            odd += 1
    if c2 > c1:
        min += c1
        if c1 % 2 == 0:
            even += 1
        else:
            odd += 1

if (min % 2 == 0 and odd > even) or (min % 2 == 1 and even > odd):
    print(min)
else:
    if min % 2 == 0 and even > odd:
        odds = []
        h = even
        l = odd
        file = open('Source/27-51b.txt', 'r')
        for i in range(0, int(file.readline())):
            c1, c2 = list(map(int, file.readline().strip().split(' ')))
            if (abs(c1 - c2) % 2 == 1):
                odds.append(abs(c1 - c2))
        odds.sort()
        b = 0
        while h > l:
            min = min + odds[b]
            h -= 1
            l += 1
            b += 1
            if (min % 2 == 1) and (even > odd):
                break
        print(min)
    if min % 2 == 1 and odd > even:
        evens = []
        j = even
        k = odd
        file = open('Source/27-51b.txt', 'r')
        for i in range(0, int(file.readline())):
            c1, c2 = list(map(int, file.readline().strip().split(' ')))
            if (abs(c1 - c2) % 2 == 1):
                evens.append(abs(c1 - c2))
        evens.sort()
        print(evens)
        o = 0
        while k > j:
            min = min + evens[o]
            print(min)
            k -= 1
            j += 1
            o += 1
            if (min % 2 == 0) and (odd > even):
                break
        print(min)