import itertools

count = 0

for i in range(1, 50):
    for commands in list(itertools.product([0, 1], repeat = i)):
        n = 8
        meet96 = False
    
        for command in commands:
            if command == 0:
                n *= 2

            if n == 96:
                meet96 = True

            if command == 1:
                n *= 3

            if n == 96:
                meet96 = True

        if meet96 and n == 3456:
            count += 1

    print(count)
