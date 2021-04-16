string = '687' * 143

while '68' in string or '7777' in string:
    string = string.replace('68', '7')
    string = string.replace('7777', '7')

print(string)
