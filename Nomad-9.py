def plus(a, b):
  if (type(a) is int or type(a) is float) and (type(b) is int or type(b) is float):
     return a + b;
  else:
    return None;

def minus(a, b):
  if (type(a) is int or type(a) is float) and (type(b) is int or type(b) is float):
     return a - b;
  else:
    return None;

def times(a, b):
  if (type(a) is int or type(a) is float) and (type(b) is int or type(b) is float):
     return a * b;
  else:
    return None;

def div(a, b):
  if (type(a) is int or type(a) is float) and (type(b) is int or type(b) is float):
     return a / b;
  else:
    return None;

def neg(a):
  if type(a) is int or type(a) is float:
     return -a;
  else:
    return None;

def power(a, b):
  if (type(a) is int or type(a) is float) and (type(b) is int or type(b) is float):
     return a ** b;
  else:
    return None;

def rem(a, b):
  return int(a) % int(b);

print(plus(5, 3));
print(plus("5", "3"));

print(minus(4, 7));
print(minus("4", 7));

print(times(3, 1));
print(times(3, "1"));

print(div(6, 4));
print(div(6, "4"));

print(neg(7));
print(neg("7"));

print(power(5, 4));
print(power("5", "4"));