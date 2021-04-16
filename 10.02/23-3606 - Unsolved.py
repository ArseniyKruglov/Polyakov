import itertools

count = 0

for n in range (-10000, 10000):
    o = n
    
    for length in range(1, 5 + 1):
        for commands in list(itertools.product([0, 1, 2], repeat = length)):
            n = o
            
            for command in commands:
                if command == 0:
                    n += 1
                    
                if command == 1:
                    n *= 2

                if command == 2:
                    n += (n % 4)

            if n == 80:
                count += 1

print(count)
