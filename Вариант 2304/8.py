import itertools

i = 0

for w in sorted(list(itertools.product('АОУ', repeat = 5))):
    w = ''.join(w)
    i += 1
    if i == 240:
        print(w)
        break
