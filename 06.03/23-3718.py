def To3(n):
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    return s

def F(s):
    global count
    n = int(s, 3)

    if s == '10':
        count += 1

    if n > int('10', 3):
        F(To3(n - 2))
        if s[-1] != '0':
            F(s[:-1] + '0')

count = 0
F('212')
print(count)
        
