n = 8 ** 152 + 4 ** 915 - 2 ** 778 - 4 ** 71 - 2 ** 31 - 30
count = 0

while (n > 0):
    if (n % 2 == 0):
        count += 1

    n //= 2

print (count)