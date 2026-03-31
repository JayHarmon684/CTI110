# P3LAB_HarmonAlbert.py
# 3/19/2026
# Description: This program collects 6 grades, then calculates
# lowest, highest, sum, average, and assigns a letter grade.


#Define constants for the change
DOLLARS = 100
QUARTERS = 25
DIMES = 10
NICKELS = 5
PENNIES = 10

#get the float from the user
change = float(input("Enter an amount as a float: $"))

#convert theh float to an interger
change = int(change * DOLLARS)
print(change)

if change == 0:
    print("no change")
    
#calculate the change for each coin type
#integer division //
# #modulus %
num_dollars = change // DOLLARS
change = change % DOLLARS

num_quarters = change // QUARTERS
change = change % QUARTERS

num_dimes = change // DIMES
change = change % DIMES

number_nickels = change // NICKELS
change = change % NICKELS

num_pennies = change // PENNIES

#Display amounts used
if num_dollars > 0:
    print(num_dollars, end=' ')
    if num_dollars == 1:
        print("Dollar")
    else:
        print("Dollars")
        
if num_quarters > 0:
    print(num_quarters, end=' ')
    if num_quarters == 1:
        print("Quarter")
    else:
        print("Quarters")   
           
        
if num_dimes > 0:
    print(num_dimes, end=' ')
    if num_dimes == 1:
        print("Dime")
    else:
        print("Dimes")
        
if number_nickels > 0:
    print(number_nickels, end=' ')
    if number_nickels == 1:
        print("Nickel")
    else:
        print("Nickels")
        
if num_pennies > 0:
    print(num_pennies, end=' ')
    if num_pennies == 1:
        print("Penny")
    else:
        print("Pennys")    