string = '5' * 150

while '5555' in string:
    string = string.replace('5555', '33')
    string = string.replace('333', '5')

print(string)
