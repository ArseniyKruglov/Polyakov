import itertools

counter = 0

for word in sorted(set(itertools.product('ИНСТАВК', repeat = 4))):
    word = ''.join(word)

    if word[0] in 'НСТВК' and word[-1] in 'ИА':
        counter += 1

    if word == 'НИКА':
        print(counter)
        break