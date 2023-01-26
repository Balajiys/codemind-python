n=int(input())
sq=n*n
ds=0
while sq:
    r=sq%10
    ds+=r
    sq=sq//10
if ds==n:
    print("Neon Number")
else:
    print("Not Neon Number")