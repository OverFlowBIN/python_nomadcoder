from math import fsum, ceil, fabs

print(ceil(1.2)) 

print(fabs(-1.2)) # absolute

print(fsum([1,2,3,4,5,5]))


import math

print(math.ceil(1.2)) 

print(math.fabs(-1.2)) # absolute

print(math.fsum([1,2,3,4,5,5]))


# as를 이용해서 import하는 module alias 설정 가능
from math import fsum, ceil, fabs as abs

print(ceil(1.2)) 

print(abs(-1.2)) # absolute

print(fsum([1,2,3,4,5,5]))

# calculator.py 를 만들고 같은 촐더 안에 있으면 import clculator import function 해서 import 할 수 있다.