import itertools

c = 0

for w in set(itertools.product('ВИШНЯ', repeat = 6)):
    w = ''.join(w)
    if w.count('В') <= 1 and w[0] != 'Ш' and w[-1] != 'И' and w[-1] != 'Я':
        c += 1

print(c)
