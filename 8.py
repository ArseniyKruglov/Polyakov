n = 4 ** 2015 + 8 ** 2016 - 2 ** 2017 - 150
s = ''

while n > 0:
    s = str(n % 2) + s
    n //= 2

print(s.count('0'))