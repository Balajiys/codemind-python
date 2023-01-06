import math
n,k,m=map(int,input().split())
a=k*m
bags=n/a
bags=math.ceil(bags)
print(bags)