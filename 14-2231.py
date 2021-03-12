# Значение арифметического выражения: 97 + 38 – 1 записали в системе счисления с основанием 3. Какая из цифр чаще всего встречается в полученном числе? В ответе укажите, сколько таких цифр в этой записи.

n = 9 ** 7 + 3 ** 8 - 1
count = [0, 0, 0]

while (n > 0):
    count[n % 3] += 1
    n //= 3

count.sort()
print (count[-1])
