def F(n):
  if n > 0: 
    G(n - 1)
def G(n):
  print("*")
  if n > 1: 
    print("*")
    F(n - 2)

F(13)
