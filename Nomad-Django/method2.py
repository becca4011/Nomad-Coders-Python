class Car():
  def __init__(self, **kwargs):
    self.doors = 4;
    self.wheels = 4;
    self.windows = 6;
    self.seats = 4;
    self.color = kwargs.get("color", "black"); #color(key)를 가져오고, 없다면 black(default)
    self.price = kwargs.get("price", "$20");#price(key)를 가져오고, 없다면 $20(default)

  #__str__ method 재정의
  def __str__(self):
    return f"Car with {self.wheels} wheels";


print(dir(Car)); #dir : class 안에 있는 모든 것을 보여줌

porche = Car(color="green", price="$40");
print(porche.color, porche.price); #지정한 값 출력
#print(porche) = print(porche.__str__())으로 작동
#string으로 바꿔 출력할 때 __str__이 호출

spark = Car();
print(spark.color, spark.price); #기본값 출력