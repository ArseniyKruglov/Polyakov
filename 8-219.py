import itertools

count = 0
look = False

for word in sorted(set(itertools.product('АКРУ', repeat = 5))):
    word = ''.join(word)

    if word == 'РУКАА':
        look = True

    if look:
        count += 1

    if word == 'УКАРА':
        print(count)
        break