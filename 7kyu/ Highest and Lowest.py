# Description

# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

# Examples
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
# Notes
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.


# My Solution
def high_and_low(numbers):
    # Split the input string into a list of numbers
    num_list = [int(num) for num in numbers.split()]
    # Find the highest and lowest numbers
    highest = max(num_list)
    lowest = min(num_list)
    # Return the highest and lowest numbers as a formatted string
    return f"{highest} {lowest}"


# Uncomment to run and check test cases
# print(high_and_low("1 2 3 4 5"))  # Output: "5 1"
# print(high_and_low("1 2 -3 4 5"))  # Output: "5 -3"
# print(high_and_low("1 9 3 4 -5"))  # Output: "9 -5"
