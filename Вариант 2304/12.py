for i in range(100 + 1, 100000):
    s = '1' * i

    while '111' in s:
        s = s.replace('111', '2')
        s = s.replace('222', '1')

    if s == '2':
        print(i)
        break
