# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [190201; 190260], числа, имеющие ровно 4 различных ЧЁТНЫХ делителя. В ответе для каждого найденного числа запишите два его наибольших ЧЁТНЫХ делителя в порядке убывания.

for i in range(190201, 190260 + 1):
    dividers = []
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            if j % 2 == 0:
                dividers.append(j)
            if i // j % 2 == 0:
                dividers.append(i // j)
    if i % 2 == 0:
        dividers.append(i)

    if len(dividers) == 4:
        dividers.sort()
        print(dividers[-1], dividers[-2])
