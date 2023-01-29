n=int(input())
if n%10==0 or n%5==0:
    ten=n//10
    remainder=n%10
    if remainder==5:
        five=1
    else:
        five=0
    print(ten+five)
else:
    print("-1")
