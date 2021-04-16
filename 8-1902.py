count = 0

for i in range(1, 100000):
    i = hex(i)[2:]

    if len(i) == 4:
        ok = True
        
        if len(set(i)) < 4:
            ok = False
        
        for j in range(0, len(i) - 1):
            if int(i[j], 16) % 2 == int(i[j + 1], 16) % 2:
                ok = False
                break
                
        if ok:
            count += 1

print(count)