import itertools

a = []

for length in range(0, 5 + 1):
    for commands in set(itertools.product([0, 1, 2], repeat = length)):
        for n in range(0, 80 + 1):
            o = n
            
            for command in commands:
                if command == 0:
                    n += 1
                elif command == 1:
                    n *= 2
                elif command == 2:
                    n += n % 4

            if n == 80:
                a.append(o)

print(len(set(a)))
