import itertools

count = 0

for word in set(itertools.permutations('РУЛЬКА')):
    word = ''.join(word)
    if word[0] != 'Ь' and 'УЬ' not in word and 'АЬ' not in word:
        count += 1


print(count)
