count = 0

for i in range(4301614, 4301717 + 1):
    prime = True

    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            prime = False
            break

    if prime:
        count += 1
        print(count, i)
