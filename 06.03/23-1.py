import sys
sys.setrecursionlimit(15000)
print(sys.getrecursionlimit())

print('Alive')

def To3(n):
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    return s

def F(s):
    global c
    n = int(s, 3)

    if s == '10':
        c += 1

    if n > 20:
        F(To3(n - 2))
        F(s[:-1] + '0')

c = 0
F('212')
print(c)
