


# Albert Harmon
# 2/10/2026
# Program # m3w210.py
# Program Desrciption: This program will demo python commands


#pseudocode
""" 3. Ask user to enter their budget

4. Ask user to enter travel destination

5. Ask user for amount they will spend on gas

6. Ask user for amount they will spend on accommodation

7. Ask user for amount they will spend on food

8. Add expenses

9. Subtract expenses from budget

10. Display results """

print("This program calculates and display travel expenses\n")
budget = float(input("Enter Budget: "))
print()
travel = input("Enter your travel destination: ")
print()
gas = float(input("How much do you think you will spend on gas: "))
print()
hotel = float(input("Approximately, how much will you need for hotel?accomodation? "))
print()
food = float(input("How much will you spend on food? "))
print("-"*12, "Travel Expenses"+"-"*12)
print("Location, travel")
print("Initial Budget:", budget)
print()
print("Fuel", travel)
print()
print("Accomodation", travel)
print()
print("Food", travel)
print()
print("Remaining Budget", budget- gas- hotel- food)

      









