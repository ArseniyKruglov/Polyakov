def To8(n):
    s = ''
    while n > 0:
        s = str(n % 8) + s
        n //= 8
    return s

count = 0
max = 0

for i in range(127, 9852 + 1):
    if i % 3 == 0 and i % 9 != 0 and len(str(i)) == len(To8(i)):
        count += 1
        max = i

print(count, max)
