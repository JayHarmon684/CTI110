# HarmonAlbert_P3HW1
# 03/24/2026
# P3HW1
# P3HW1 - Module Grades List Stats

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

# grades list
grade_list = []

# get grades from the user
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

# add the grades to the list
gradeList = [grade1, grade2, grade3, grade4, grade5, grade6]

lowest = min (gradeList)
highest= max(gradeList)
total = sum(gradeList)
avg = sum(gradeList)/len(gradeList)

# print results
print("\n------------Results------------")
print(f"{'Lowest Grade:':<15}{lowest:>6.2f}")
print(f"{'Highest Grade:':<15}{highest:>6.2f}")
print(f"{'Sum of Grades:':<15}{total:>6.2f}")
print(f"{'Average:':<15}{avg:>6.2f}")

print("--------------------------------")
