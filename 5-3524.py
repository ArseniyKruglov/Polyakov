answer = 0

for n in range (1, 100000):
    new_n = ''
    while n > 0:
        new_n = str(n % 6) + new_n
        n //= 6

    new_n += new_n[-1]
    new_n = int(new_n, 6)
    new_n = bin(new_n)[2:]
    new_n += new_n[-1]
    new_n = int(new_n, 2)

    if new_n < 344:
        answer = new_n

print(answer)