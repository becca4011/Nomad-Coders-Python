#tuple(immutable sequence - sequence 변경 불가능), () 사용
days = ("Mon", "Tue", "Wed", "Thur", "Fri");

print(type(days));

#dictionary, {} 사용
info = {
  "name" : "Name",
  "age" : 21,
  "korean" : True,
  "fav_food" : ["Kimchi", "Pizza"]
}

print(type(info));

print(info["name"]);
print(info["age"]);

print(info);
info["woman"] = True;
print(info);