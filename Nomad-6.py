def p_plus(a, b):
  print(a + b);
  #콘솔에 print만 함
  #return을 하지 않았으므로 None

def r_plus(a, b):
  return a + b;
  print("hello");
  #function 밖으로 값을 보냄
  #return은 function을 종료(print 실행 X)
  #function 안에는 return을 한번만 할 수 있음

p_result = p_plus(2, 3);
r_result = r_plus(2, 3); #호출

print(p_result, r_result);