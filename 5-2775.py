array = []

for i in range(20, 600 + 1):
    array.append(int(bin(i)[2:-2], 2))

print(len(set(array)))