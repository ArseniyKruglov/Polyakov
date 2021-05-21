for i in range(-1000, 1000):
    x = i
    a = 1 
    b = 0
    while x > 0: 
      c = x % 10
      a = a*c
      if c > b: b = c
      x = x // 10
    if a == 48 and b == 6:
        print(i)
