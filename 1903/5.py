for i in range(1, 256 + 1):
    n = i
    i = bin(i)[2:]
    
    invert = False
    s = ''
    for j in range(len(i) - 1, 0 - 1, -1):
        if invert:
            if i[j] == '1':
                s = '0' + s
            else:
                s = '1' + s
        else:
            s = i[j] + s
            
        if i[j] == '1':
            invert = True
            
    if int(s, 2) == 98:
        print(n)