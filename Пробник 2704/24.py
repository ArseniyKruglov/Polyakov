file = open('24-s1.txt', 'r')
lines = file.readlines()

a = []

for line in lines:
    a.append(line.count('Q'))



line = lines[a.index(max(a))]

for char in sorted(list(set(line))):
    print(char, line.count(char))

c = 0
for line in lines:
    c += line.count('C')
print(c)
