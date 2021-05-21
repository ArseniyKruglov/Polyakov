array = []

for i in range(1905, 9868 + 1):
    if i % 3 == 0 and i % 23 != 0:
        array.append(i)

print(len(array), sum(array))
