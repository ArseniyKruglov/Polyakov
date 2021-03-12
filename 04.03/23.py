import itertools

a = []
c = 0

for commands in set(itertools.product([0, 1, 2], repeat = 6)):
    n = 1
    for command in commands:
        if command == 0:
            n += 1
        elif command == 1:
            n += 2
        elif command == 2:
            n *= 2
    a.append(n)

for n in set(a):
    if 34 <= n and n <= 59:
        c += 1

print(c)
        
