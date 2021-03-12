for i in range(0, 2 ** 4):
    w = i % 2
    z = i // 2 % 2
    y = i // 4 % 2
    x = i // 8 % 2

    if not x and y and z or x and not y and not x:
        print(x, y, z, w, ' ', 1)

# Возможно, некорректное условие
