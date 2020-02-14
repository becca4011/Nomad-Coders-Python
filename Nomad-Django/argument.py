#positional argument
def plus(*args):
  result = 0;

  for num in args:
    result += num;
  
  print(result);

plus(1, 2, 1, 3, 4, 1, 2, 1);

#keyword argument
def ka(**kwargs):
  print(kwargs);

ka(hello = "Hello", hi = "Hi", bye = "Bye");