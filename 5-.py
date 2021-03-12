n = 95
n = bin(n)
n = '0' + n[2:]

n_reversed = ''
for char in n:
    if char == '1':
        n_reversed += '0'
    else:
        n_reversed += '1'

n_reversed = int(n_reversed, 2)
n_reversed += 1

print(n_reversed)
