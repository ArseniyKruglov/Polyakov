n = (729 ** 41 - 81 ** 16) * (729 ** 15 + 9 ** 5)
count = 0

while (n > 0):
    if (n % 9 == 0):
        count += 1

    n //= 9

print(count)