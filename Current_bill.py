x=int(input())
if x>=600:
    bill=x*2
elif x>=400:
    bill=x*1.8
elif x>=200:
    bill=x*1.5
else:
    bill=x*1.2
if bill>=400:
    finalbill=bill+bill*0.15
    print("{:.2f}".format(finalbill))
else:
    finalbill=bill+100
    print("{:.2f}".format(finalbill))