count = 0
min_n = 0

for i in range(980, 5320):
    if (i % 4 == 0 or i % 5 == 0) and i % 11 != 0 and i % 17 != 0 and i % 19 != 0 and i % 23 != 0:
        if count == 0:
            min_n = i

        count += 1

print(count, min_n)
