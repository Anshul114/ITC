Rate = 0.2
SD = 10000          #standard deduction
AD = 3000           #additional deduction

Gross = int(input("Gross income: "))
Dependents = int(input("Number of Dependents: "))

tax_income = Gross - SD -(AD*Dependents)

print(tax_income)