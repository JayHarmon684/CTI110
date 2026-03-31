#P3HW2_HarmonAlbert

#3/24/2026

#P3HW2_HarmonAlbert

#calculate overtime pay


#Asks the user to enter name of employee
name = input("Enter employees name: ")
hoursWorked = float(input("Enter number of hours worked: "))
payRate = float(input("Enter Employee pay rate: "))

#calculate overtime using an if/else decision structure
if hoursWorked > 40:
    # calculate overtime
    overTimeHours = hoursWorked - 40
    # calculate over time pay
    overPay = overTimeHours * (payRate * 1.5)
    # calculate salary for reg hours worked
    regPay = 40 * payRate
    # calculate gross pay
    grossPay = regPay + overPay
else:
    overPay = 0
    overTimeHours = 0
    regPay = hoursWorked * payRate
    grossPay = regPay
    
print("-"*20)
print("Employee name: ",name, "\n")

print(f'{'Hours Worked':<15}{"Pay Rate":<12}{"Over Time":<12}{"Over Time Pay":<20}{"RegHour Pay":<20}{"Gross Pay":<20}')
print("-"*95)
print(f'{hoursWorked:<15}{payRate:<12}{overTimeHours:<12}{overPay:<20}{regPay:<20}{grossPay:<20}')












'''
print(overPay)
print(overTimeHours)
print(regPay)
print(grossPay)
'''
    


















