# Description

# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

# Example(Input => Output):
# 35231 => [1,3,2,5,3]
# 0 => [0]


# My Solution
def digitize(n):
    # Convert the number to a string, reverse it, and convert each character to an integer
    reversed_digits = [int(digit) for digit in str(n)[::-1]]

    return reversed_digits


# Uncomment to run and check test case
# print(digitize(35231))  # Output: [1, 3, 2, 5, 3]
# print(digitize(0))  # Output: [0]
