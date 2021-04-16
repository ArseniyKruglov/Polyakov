import itertools

c = 0

for word in set(itertools.permutations('РУЛЬКА')):
    word = ''.join(word)
    if word[0] != 'Ь' and 'УЬ' not in word and 'АЬ' not in word:
        c += 1


print(c)
