for i in range(1, 256):
    bin_ = bin(i)[2:]
    bin_ = '0' * (8 - len(bin_)) + bin_
    
    bin_r = ''
    for char in bin_:
        if char == '0':
            bin_r += '1'
        else:
            bin_r += '0'

    if int(bin_r, 2) + 1 == 221:
        print(i)
