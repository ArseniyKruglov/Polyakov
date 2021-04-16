import itertools

count = []

for word in list(itertools.product('КАНТ', repeat = 6)):
    word = ''.join(word)
    if word.count('К') == 2:
        count.append(word)

print(len(set(count)))
