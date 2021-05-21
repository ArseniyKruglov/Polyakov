file = open('24.txt', 'r')
string = file.readline()

max_count = 0
max_char = ''
max_index = 100000

for char in 'QWERTYUIOPASDFGHJKLZXCVBNM0123456789':
    for i in range(0, 1000):
        if char * i in string:
            if i >= max_count:
                max_count = i
                max_char = char

                print(string.index(char * i), max_char, max_count) 
