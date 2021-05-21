array = []

for i in range(777, 19990 + 1):
    if max(map(int, oct(i)[2:])) == 6 and (i % 11 == 0 or i % 13 == 0) and i % 15 != 0:
        array.append(i)

print(len(array), max(array) - min(array))
