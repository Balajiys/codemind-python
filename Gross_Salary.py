BS=int(input())
if BS>20000:
    GS=(BS+0.95*BS+0.3*BS)
    print("{:.2f}".format(GS))
elif BS>10000 and BS<=20000:
    GS=(BS+0.90*BS+0.25*BS)
    print("{:.2f}".format(GS))
else:
    GS=(BS+0.80*BS+0.20*BS)
    print("{:.2f}".format(GS))