# Harmon Albert    
# 02/24/2026
# P2LAB1HarmonAlbert.py
# This program will calculate the diameter,area circumference of a circle.

# Import the math library for the constant pi

import math

# Get radius from user
radius = float(input("What is the radius of the circle? "))
print()

# Calculate the diameter
diameter = 2 * radius

# Display diameter with one decimal place
print(f"The diameter of the circle is? {diameter:.1f}\n")

# Calculate the circumference
circumference = 2 * math.pi * radius

# Display circumference with two decimal places
print(f"The circumference of the circle is? {circumference:.2f}\n")

# Calculate the area
area = math.pi * radius ** 2

# Display area with two decimal places
print(f"The area of the circle is? {area:.3f}\n")


