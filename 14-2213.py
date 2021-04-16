n = 9 ** 20 + 3 ** 60 - 15
s = ''

while n > 0:
    s = str(n % 3) + s
    n //= 3

print(s.count('2'))