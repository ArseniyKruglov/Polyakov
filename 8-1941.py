import itertools

count = 0

for word in set(itertools.permutations('НОБЕЛИЙ', 7)):
    word = ''.join(word)

    if word[0] != 'Й' and 'ИЙО' not in word:
        count += 1

print(count)