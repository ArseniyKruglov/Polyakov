import itertools

c = 0

for word in set(itertools.permutations('АДЖИКА', 6)):
    word = ''.join(word)
    if 'АА' not in word:
        c += 1

print(c)
