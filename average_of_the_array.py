n=int(input())
lst=list(map(int,input().split()))
sum_of_array=sum(lst)
average=sum_of_array/n
print("{:.2f}".format(average))