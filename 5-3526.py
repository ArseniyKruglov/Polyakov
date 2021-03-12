max = 0

for n in range (1, 256):
    n8 = ''
    while (n > 0):
        n8 = str(n % 8) + n8
        n //= 8

    n8_r = n8[::-1]
    diff = int(n8, 8) - int(n8_r, 8)

    print(diff)
