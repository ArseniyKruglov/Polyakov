def To4(n):
    s = ''
    while n > 0:
        s = str(n % 4) + s
        n //= 4
    return s

def F(s):
    n = int(s, 4)
    
    if s == '100':
        global count
        count += 1

    if n < int('100', 4):
        F(To4(n + 2))
        F(To4(n + 3))
        F(s + '0')

count = 0
F('1')
print(count)