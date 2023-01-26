n=int(input())
if n<0:
    is_negative=True
    n=-n
else:
    is_negative=False
rev=0
while n:
    r=n%10
    rev=rev*10+r
    n=n//10
if is_negative==True:
    print(-rev)
else:
    print(rev)