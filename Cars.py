import math
n=int(input())
if n<=4:
    cars=1
else:
    a=n/4
    cars=math.ceil(a)
print(cars)