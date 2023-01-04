n=int(input())
sum1=0
sum2=0
for i in range(1,n+1):
    x=i*i
    sum1=sum1+x
for i in range(1,n+1):
    sum2=sum2+i
    y=sum2*sum2
difference=sum1-y
print(abs(difference))
    