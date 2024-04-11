# Description

# You ask a small girl,"How old are you?" She always says, "x years old", where x is a random number between 0 and 9.

# Write a program that returns the girl's age (0-9) as an integer.

# Assume the test input string is always a valid string. For example, the test input may be "1 year old" or "5 years old". The first character in the string is always a number.


# My Solution
def get_age(age):
    return int(age[0])


# Uncomment to run and check test cases
# print(get_age("5 years old"))  # Output: 5
# print(get_age("9 years old"))  # Output: 9
# print(get_age("3 years old"))  # Output: 3
