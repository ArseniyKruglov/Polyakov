file = open('Source/24-2536.txt', 'r')
string = file.readline()

length = 0
max_length = 0
answer = 0

for i in range(0, len(string) - 1):
    if (ord(string[i]) > ord(string[i + 1])):
        length += 1
    else:
        length += 1
        
        if (length > max_length):
            max_length = length
            answer = i - length + 1 + 1
        
        length = 0

print(answer)