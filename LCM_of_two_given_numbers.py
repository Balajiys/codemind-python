m,n=map(int,input().split())
if m>n:
    greater=m
else:
    greater=n
while True:
    if greater%m==0 and greater%n==0:
        lcm=greater
        break
    greater+=1
print(lcm)