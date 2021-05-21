c = 0

for i in range(3721, 7752 + 1):
    if sum(list(map(int, str(i)))) % 3 == 0 and bin(i)[-4: -1] != '000':
        if c == 0:
            print(i)
            
        c += 1

print(c)
