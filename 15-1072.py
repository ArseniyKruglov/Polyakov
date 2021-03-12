# Укажите наибольшее целое значение А, при котором выражение (3y + 2x ≠ 130) ∨ (3x > A) ∨ (2y > A) истинно для любых целых положительных значений x и y.

for A in range(0, 1000):
    ok = True

    for x in range(1, 1000):
        for y in range(1, 1000):
            if not((3 * y + 2 * x != 130) or (3 * x > A) or (2 * y > A)):
                ok = False
                break

        if not ok:
            break

    if ok:
        print(A)
