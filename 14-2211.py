n = (729 ** 41 - 81 ** 16) * (729 ** 15 + 9 ** 5)
c = 0

while (n > 0):
    if (n % 9 == 0):
        c += 1

    n //= 9

print(c)
