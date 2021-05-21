import itertools
print(list(itertools.permutations('abc')))

for b in range(2):
    for a in range(2):
        for c in range(2):
            print(b, a, c, ' ', 1 if not a or (b and not c) else 0)
