def age_check(age):
  print(f"you are {age}");

  if age < 20:
    print("you can't drink");
  elif age == 20: #elif = else if
    print("you are new to this!");
  elif age > 20 and age < 25:
    print("you are still kind of young");
  else:
    print("you can drink");

age_check(29);