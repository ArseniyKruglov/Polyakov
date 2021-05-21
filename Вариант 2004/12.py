string = '>' + 25 * '1' + 17 * '2' + 10 * '3'

while '>1' in string or '>2' in string or '>3' in string:
    if '>1' in string:
        string = string.replace('>1', '22>3')

    if '>2' in string:
        string = string.replace('>2', '2>')

    if '>3' in string:
        string = string.replace('>3', '11>2')

print(sum(list(map(int, string.replace('>', '')))))
