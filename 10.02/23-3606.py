import itertools

c = 0

for length in range(1, 50):
    for commands in list(itertools.product([0, 1], repeat = length)):
        n = 24

        for command in commands:
            if command == 0:
                n += 1

            if command == 1:
                s = ''
                
                for char in str(n):
                    if int(char) != 9:
                        s += str(int(char) + 1)
                    else:
                        s += str(int(char))
                
                n = int(s)

        if n == 46:
            c += 1

    print(c)
