n=int(input())
if n>=800:
    rate=2.00
elif n>=600:
    rate=1.80
elif n>=400:
    rate=1.60
elif n>=200:
    rate=1.40
else:
    rate=1.20
bill=rate*n
if bill>400:
    sur=bill*0.15
else:
    sur=0
print("Units Consumed:",n)
print("Cost per Unit: {:.2f}".format(rate))
print("Bill: {:.2f}".format(bill))
print("Surcharge: {:.2f}".format(sur))
print("Total Amount: {:.2f}".format(bill+sur))
