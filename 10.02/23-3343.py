import itertools

c = 0

for commands in set(list(itertools.product([0, 1, 2], repeat = 6))):
    n = 1

    for command in commands:
        if command == 0:
            n += 1

        if command == 1:
            n += 1

        if command == 2:
            n *= 2
            
    if n == 20:
        c += 1

print(c)
