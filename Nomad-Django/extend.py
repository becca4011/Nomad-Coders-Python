class Car():
  def __init__(self, **kwargs):
    self.doors = 4;
    self.wheels = 4;
    self.windows = 6;
    self.seats = 4;
    self.color = kwargs.get("color", "black");
    self.price = kwargs.get("price", "$20");

  def __str__(self):
    return f"Car with {self.wheels} wheels";

class Convertible(Car): #Convertible class안에 Car class가 있음(extend))
  def __init__(self, **kwargs):
    super().__init__(**kwargs); 
    #super() : 부모 class(Car)를 호출하는 함수
    #()안에 **kwargs를 넣지 않으면 기본값으로만 출력됨
    self.time = kwargs.get("time", 10);

  def take_off(self):
    return "taking off";

  def __str__(self):
    return "Car with no roof";

porche = Convertible(color="blue");
print(porche.color); #super()로 부모 class를 호출하지 않으면 오류 발생