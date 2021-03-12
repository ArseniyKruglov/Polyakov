def To4(n):
    s = ''
    while n > 0:
        s = str(n % 4) + s
        n //= 4
    return s

def F(s):
    global c
    n = int(s, 4)
    
    if s == '100':
        c += 1

    if n < int('100', 4):
        F(To4(n + 2))
        F(To4(n + 3))
        F(s + '0')

c = 0
F('1')
print(c)
