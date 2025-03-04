# Package Express Shipping Calculator
# Author: Jennifer Lee
# Version: 1.5.0

# Display welcome message
print("Welcome to Package Express. Please follow the instructions below.")

# Get package weight from user
weight_input = float(input("Please enter the package weight:\n"))

# Check if weight exceeds limit
if weight_input > 50:
    print("Package too heavy to be shipped via Package Express. Have a good day.")
    exit()

# Get package dimensions
width_input = float(input("Please enter the package width:\n"))
height_input = float(input("Please enter the package height:\n"))
length_input = float(input("Please enter the package length:\n"))

# Calculate total package size
total_size = width_input + height_input + length_input

# Check if size exceeds limit
if total_size > 50:
    print("Package too big to be shipped via Package Express.")
    exit()

# Calculate shipping cost
# Formula: (width * height * length * weight) / 100
shipping_cost = (width_input * height_input * length_input * weight_input) / 100

# Display shipping cost
print(f"Your estimated total for shipping this package is: ${shipping_cost:.2f}")
print("Thank you!") 