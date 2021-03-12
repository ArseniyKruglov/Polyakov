import itertools

c = []

for word in list(itertools.product('КАНТ', repeat = 6)):
    word = ''.join(word)
    if word.count('К') == 2:
        c.append(word)

print(len(set(c)))
