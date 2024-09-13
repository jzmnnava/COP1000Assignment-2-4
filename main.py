#input statements
#salary = 1250.00 
#numDependents = 2

salary = float(input("Enter your salary: "))
numDependents = float(input("Enter the number of dependents: "))

# calculate taxes here
stateTax = salary * 0.065
federalTax = salary * 0.28
dependentDeduction = numDependents * (0.025 * salary)
totalWithholding = stateTax + federalTax + dependentDeduction 
takeHomePay = salary - totalWithholding 

# output statements
print("State Tax: $" + str(stateTax))
print("Fedral Tax: $" + str(federalTax))
print("Dependents: $" + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
