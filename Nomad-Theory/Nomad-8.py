def plus(a, b):
  return int(a) + int(b);

def minus(a, b):
  return int(a) - int(b);

def times(a, b):
  return int(a) * int(b);

def div(a, b):
  return int(a) / int(b);

def neg(a):
  return -int(a);

def power(a, b):
  return int(a) ** int(b);

def rem(a, b):
  return int(a) % int(b);

plus = plus("6", 4);
minus = minus(6, "4");
times = times("6", "4");
div = div(6, "4");
neg = neg(6);
power = power("6", 4);
rem = rem(6, 4);

print(f"plus = {plus}, minus = {minus}, times = {times}, div = {div}, negation = {neg}, power = {power}, remainder = {rem}");