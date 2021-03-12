# Для какого наименьшего целого неотрицательного числа А выражение (5x – 6y < A) ∨ (x – y > 30) тождественно истинно, т.е. принимает значение 1 при любых целых неотрицательных x и y?

for A in range(0, 1000):
    ok = True

    for x in range(0, 1000):
        for y in range(0, 1000):
            if not((5 * x - 6 * y < A) or (x - y > 30)):
                ok = False
                break

        if not ok:
            break

    if ok:
        print(A)
        break
