n=int(input())
r=n%2
if r==1:
    print("weird")
elif r==0 and n>=2 and n<=5:
    print("not weird")
elif r==0 and n>=6 and n<=20:
    print("weird")
elif r==0 and n>20:
    print("not weird")