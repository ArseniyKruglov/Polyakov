for i in range(-1000, 1000):
    x = i
    a = 1
    while x > 0:
      a *= x % 9
      x = x // 9

    if a == 60:
        print(i)
        break
