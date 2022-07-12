def say_hello(who='anonymous'):
  print('hello', who)
  print('bye')  

say_hello() 

def plus(a, b):
  print(a + b)

def minus(a, b = 0):
  print(a - b)

plus(2, 5)
minus(2)