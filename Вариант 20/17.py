c = 0
s = 0

for i in range(2595, 8401 + 1):
    if i % 2 == 0 and i % 13 != 0:
        c += 1
        s += i

print(c, s)
