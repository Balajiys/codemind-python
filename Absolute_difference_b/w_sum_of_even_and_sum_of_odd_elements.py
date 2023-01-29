n=int(input())
lst=list(map(int,input().split()))
oddsum=evensum=0
for i in range(n):
    if lst[i]%2==0:
        evensum=evensum+lst[i]
    else:
        oddsum=oddsum+lst[i]
difference=abs(oddsum-evensum)
print(difference)