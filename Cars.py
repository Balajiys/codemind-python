import math
n=int(input())
if n<=4:
    cars=1
else:
    cars=n/4
cars=math.ceil(cars)
print(cars)