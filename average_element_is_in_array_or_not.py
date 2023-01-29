n=int(input())
lst=list(map(int,input().split()))
average=sum(lst)//n
flag=0
for i in range(n):
    if average==lst[i]:
        flag=1
        break
if flag==1:
    print("True")
else:
    print("False")