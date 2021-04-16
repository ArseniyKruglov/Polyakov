import itertools

for i in range(100, 1000):
    array = []
    
    for n in list(itertools.permutations(str(i), 2)):
        n = ''.join(n)
        n = int(n)
        if n >= 10:
            array.append(n)

    if max(array) - min(array) == 14:
        print(i)
