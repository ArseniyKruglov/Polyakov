import itertools

c = 0

for w in set(itertools.product('←→↑↓', repeat = 5)):
    w = ''.join(w)
    if w[0] != '↑' and w != w[::-1]:
        c += 1

print(c)
