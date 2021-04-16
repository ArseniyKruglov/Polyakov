a = []

for i in range(20, 600 + 1):
    a.append(int(bin(i)[2:-2], 2))

print(len(set(a)))
    
