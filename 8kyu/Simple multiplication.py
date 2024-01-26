# Description

# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.


# My Solution
def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9


# Uncomment to run and check test cases
# print(simple_multiplication(4))  # Output: 32 (4 is even, multiplied by 8)
# print(simple_multiplication(7))  # Output: 63 (7 is odd, multiplied by 9)
