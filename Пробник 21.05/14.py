n = 7 * 512 ** 120 - 6 * 64 ** 100 + 8 ** 210 - 255

s = ''
while n > 0:
    s = str(n % 8) + s
    n //= 8

print(s.count('0'))
