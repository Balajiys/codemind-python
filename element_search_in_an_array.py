n=int(input())
lst=list(map(int,input().split()))
check=int(input())
flag=0
for i in range(n):
    if lst[i]==check:
        flag=1
        break
if flag==1:
    print("True")
else:
    print("False")