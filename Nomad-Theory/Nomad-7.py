#Keyworded Arguments
def say_hello(name, age, are_from, fav_food):
  return f"Hello {name} you are {age} years old. You are from {are_from}. You like {fav_food}."; #f : format
  #return "Hello" + name + " you are " + age + " years old";

hello = say_hello(age="21", name="none", fav_food="kimchi", are_from="korea");
print(hello);