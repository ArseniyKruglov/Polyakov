n = 9 ** 7 + 3 ** 8 - 1
count = [0, 0, 0]

while (n > 0):
    count[n % 3] += 1
    n //= 3

print(max(count))