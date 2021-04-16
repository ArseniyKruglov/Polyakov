answer = 0

for n in range (1, 256):
    n = bin(n)[2:]
    n = '0' * (8 - len(n)) + n
    difference = int(n, 2) - int(n[::-1], 2)

    answer = max(answer, difference)

print(answer)