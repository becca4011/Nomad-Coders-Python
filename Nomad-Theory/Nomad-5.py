def say_hello(who="everyone"):
  print("hello", who);

say_hello("name");
say_hello();

def plus(a, b):
  print(a + b);

def minus(a, b=0): #b=0 : default value
  print(a - b);

plus(2, 5);
minus(2);