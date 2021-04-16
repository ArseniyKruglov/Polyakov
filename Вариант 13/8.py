import itertools

c = 0

for word in list(itertools.permutations('ВЕНТИЛЬ', 7)):
    word = ''.join(word)
    if word[-1] != 'Ь' and 'ЕЬИ' not in word and 'ИЬЕ' not in word:
        c += 1

print(c)
