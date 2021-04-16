for i in range(100 + 1, 100000):
    x = i
    L = x - 16
    M = x + 16
    while L != M:
      if L > M:
        L = L - M
      else:
        M = M - L

    if M == 16:
        print(i)
        break
