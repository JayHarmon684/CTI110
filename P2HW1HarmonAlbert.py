#P2HW1_HarmonAlbert
# 03/03/2026
# P2HW1 - Travel Expenses
# This program asks the user for a travel budget and expenses, then displays a neatly formatted summary and remaining balance.

print("This program calculates and displays travel expenses\n")

# Get inputs (convert money values to float)

budget = float(input("Enter Budget: "))

destination = input("\nEnter your travel destination: ")

gas = float(input("\nHow much do you think you will spend on gas? "))

hotel = float(input("\nApproximately, how much will you need for accomodation/hotel? "))

food = float(input("\nLast, how much do you need for food? "))

# Calculations
total_expenses = gas + hotel + food
remaining = budget - total_expenses

# Formatted output
print("-" *12 + "Travel Expenses"+ "-" *12)
print(f"{'Location:':<20}{destination:>15}")
print(f"{'Initial Budget:':<20}${budget:>14.2f}")
print(f"{'Fuel:':<20}${gas:>14.2f}")
print(f"{'Accomodation:':<20}${hotel:>14.2f}")
print(f"{'Food:':<20}${food:>14.2f}")
print("-" * 41)
print(f"{'Remaining Balance:':<20}${remaining:> .2f}")