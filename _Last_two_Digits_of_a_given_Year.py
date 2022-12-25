y=int(input())
last_digit=y%10
temp=y//10
last_butone_digit=temp%10
print("{}{}".format(last_butone_digit,last_digit))