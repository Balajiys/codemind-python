n=int(input())
c=0
while n>0:
    d=n%10
    if c<d:
        c=d
    else:
        c=c
    n=n//10
print(c)
    