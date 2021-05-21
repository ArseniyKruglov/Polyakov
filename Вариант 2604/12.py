string = 3 * '2' + (21 - 3) * '5'

while '222' in string or '888' in string:
    while '555' in string:
        string = string.replace('555', '8')
    if '222' in string:
        string = string.replace('222', '8')
    else:
        string = string.replace('888', '2')

print(string)
