# Description

# We need a function that can transform a string into a number. What ways of achieving this do you know?

# Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.

# Examples
# "1234" --> 1234
# "605"  --> 605
# "1405" --> 1405
# "-7" --> -7


# My Solution
def string_to_number(s):
    # Use the int() function to convert the string into an integer
    number = int(s)
    return number

# Uncomment to run and check test case
# number1 = string_to_number("1234")   # This will return 1234
# print(number1)
