n = 36 ** 27 + 6 ** 18 - 19
s = ''

while n > 0:
    s = str(n % 6) + s
    n //= 6

print(s.count('0'))
