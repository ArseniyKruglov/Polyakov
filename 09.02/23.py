import itertools

a = [0, 1]
c = []

l = list(itertools.product(a, repeat = 8))

for commands in l:
    n = 1
    
    for command in commands:
        if command == 0:
            n += 1

        if command == 1:
            n += 5
            
        if command == 2:
            n *= 3

    if 1000 <= n and n <= 1024:
        c.append(n)

print(len(set(c)))
