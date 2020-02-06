import math; #module을 불러옴

print(math.ceil(1.2));
print(math.fabs(-1.2));

from math import ceil, fsum as sum_all; #이름을 바꿀 수 있음

print(ceil(2.1));
print(sum_all([1, 2, 3, 4, 5, 6, 7]));

from calculator import plus, minus; #calculator 파일에 정의된 함수를 가져옴

print(plus(1, 2), minus(1, 2));