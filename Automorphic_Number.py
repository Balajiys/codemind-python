n=int(input())
sq=n*n
t=str(n)
d=sq%10**len(t)
if d==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")

    