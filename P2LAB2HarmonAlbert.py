# Harmon Albert    
# 02/26/2026
# P2LAB2HarmonAlbert.py
# This project will demo the use of dictionaries.


# Create the dictionary The car model is key and the mpg is the value.
cars = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Display results show a list of all keys in the dicitonary
keys = cars.keys()
print(keys)
print()
# Get user input get the vehicle from the user
car_input = input("Enter a vehicle to see its mpg:")
print( )
#Get the corresponding mpg to the vehicle name
mpg_output = cars[car_input]
# Display output
print(f"The {car_input} gets {mpg_output} mpg.\n")
# Get the distance traveled from the user
distance = float(input("How many miles will you drive the {car_input}? "))
print()
#calculate gallons of gas needed
gallons_needed = distance / mpg_output
# Display the car and the gallons needed
print(f"{gallons_needed:,.2f} gallons of gas needed to drive the {car_input} {distance} miles.")
