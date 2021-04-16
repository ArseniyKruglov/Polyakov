n = 9 ** 7 + 3 ** 21 - 9
s = ''

while n > 0:
    s = str(n % 3) + s
    n //= 3

print(s.count('2'))
