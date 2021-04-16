for i in range(1, 256):
    binary = bin(i)[2:]
    binary = '0' * (8 - len(binary)) + binary
    binary = binary.replace('0', '2').replace('1', '0').replace('2', '1')
    binary = int(binary, 2)
    binary += 1
    
    if binary == 221:
        print(i)