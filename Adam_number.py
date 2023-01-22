n=int(input())
sq=n*n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
x=rev*rev
y=0
while x:
    r=x%10
    y=y*10+r
    x=x//10
if sq==y:
    print("True")
else:
    print("False")