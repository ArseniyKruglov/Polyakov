import itertools

for i in range(540, 540 + 1):
    a = []
    
    for n in list(itertools.permutations(str(i), 2)):
        n = ''.join(n)
        n = int(n)
        if n >= 10:
            a.append(n)

    if max(a) - min(a) == 14:
        print(i)
