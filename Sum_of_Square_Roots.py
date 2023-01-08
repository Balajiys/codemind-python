import math
a,b=map(int,input().split())
sum=0
for i in range(a,b+1):
    x=math.sqrt(i)
    sum=sum+x
print("{:.2f}".format(sum))