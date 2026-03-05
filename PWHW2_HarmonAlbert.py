#HarmonAlbert_P2HW2
# 03/03/2026
# P2HW2 - Module Grades List Stats

"""
PSEUDOCODE (Detail Algorithm)
1. Display a message that the program will collect module grades.
2. Ask the user to enter 6 grades (Module 1 through Module 6), one at a time.
3. Convert each grade to float and store each one in a list named module_grades.
4. Calculate:
   - lowest grade in the list
   - highest grade in the list
   - sum of grades
   - average of grades
5. Display the results in a neatly formatted output.
   - Average must show exactly two decimal places.
"""

# Collect grades (each requested in a separate statement)
module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

# Store grades in a list with a descriptive name
module_grades = [module1, module2, module3, module4, module5, module6]

# Calculations
lowest_grade = min(module_grades)
highest_grade = max(module_grades)
sum_of_grades = sum(module_grades)
average_grade = sum_of_grades / len(module_grades)

# Output (formatted)
print("\n------------Results------------")
print(f"{'Lowest Grade:':<15}{lowest_grade:>8.2f}")
print(f"{'Highest Grade:':<15}{highest_grade:>8.2f}")
print(f"{'Sum of Grades:':<15}{sum_of_grades:>8.2f}")
print(f"{'Average:':<15}{average_grade:>8.2f}")
print("--------------------------------")