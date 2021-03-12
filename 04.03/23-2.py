def F(top, down, type):
    if top == down:
        a[type] += 1

    if top > 2:
        F(top - 2, down, type)

    if top > 3:
        F(top - 3, down, type)

    if top % 10 == 1 and top > 10:
        F(top // 10, down, type)

a = [0, 0]

F(25, 12, 0)
F(12, 3, 1)

print(a[0] * a[1])
