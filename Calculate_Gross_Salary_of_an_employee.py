basic_salary=float(input())
HRA=float(input())
DA=float(input())
pf=0.12*basic_salary
gross_salary=basic_salary+HRA+DA+pf
print("{:.2f}".format(pf))
print("{:.2f}".format(gross_salary))