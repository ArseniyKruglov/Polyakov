import itertools

c = 0

for word in sorted(list(itertools.product('ИНСТАВК', repeat = 4))):
    word = ''.join(word)

    if word[0] in 'НСТВК' and word[-1] in 'ИА':
        c += 1

    if word == 'НИКА':
        print(c)
        break
