class Car():
  doors = 4;
  wheels = 4;
  windows = 6;
  seats = 4;

  #method : class 안에 있는 function
  def start(self): #self : argument
    print("Car");

#파이썬은 method(start)를 호출한 instance(mini)를 첫번째 argument로 사용
mini = Car();
mini.start(); # mini.start() → mini.start(mini)