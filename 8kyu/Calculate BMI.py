# Description

# Write function bmi that calculates body mass index (bmi = weight / height2).

# if bmi <= 18.5 return "Underweight"

# if bmi <= 25.0 return "Normal"

# if bmi <= 30.0 return "Overweight"

# if bmi > 30 return "Obese"


# My Solution
def bmi(weight, height):
    # Calculate BMI
    bmi_value = weight / (height ** 2)

    # Determine the category based on BMI
    if bmi_value <= 18.5:
        return "Underweight"
    elif bmi_value <= 25.0:
        return "Normal"
    elif bmi_value <= 30.0:
        return "Overweight"
    else:
        return "Obese"

# Uncomment to run and check test cases
# print(bmi(70, 1.75))  # Output: "Normal"
# print(bmi(55, 1.65))  # Output: "Normal"
# print(bmi(90, 1.80))  # Output: "Overweight"
# print(bmi(100, 1.70)) # Output: "Obese"
