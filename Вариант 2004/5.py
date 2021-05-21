for i in range(1, 256):
    bin_ = bin(i)[2:]
    bin_ = (8 - len(bin_)) * '0' + bin_

    bin_to_rev = bin_[0 : bin_[::-1].index('1') + 1]
    bin_not_to_rev = bin_[bin_[::-1].index('1'): -1]
    
    print(bin_, bin_to_rev + bin_not_to_rev)
