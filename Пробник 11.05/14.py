n = 9 ** 7 - 3 ** 12 + 3 ** 25 - 19
s = ''

while n > 0:
    s += str(n % 3)
    n //= 3

print(s.count('2'))
