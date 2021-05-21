for i in range(-1000, 1000):
    s = i
    n = 0
    while s*s < 101:
      s = s + 1
      n = n + 2

    if n == 16:
        print(i)
        break
