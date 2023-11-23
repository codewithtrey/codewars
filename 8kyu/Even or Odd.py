# Description
# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.


# My Solution
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Uncomment to run and check test cases
# number = 6
# print(even_or_odd(number))
