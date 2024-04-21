# Description

# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

# Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

# Note: The function accepts an integer and returns an integer.

# Happy Coding!

# My Solution
def square_digits(num):
    # Convert number to string and iterate over each digit
    squared_digits = ''.join(str(int(digit) ** 2) for digit in str(num))
    # Convert concatenated squared digits back to integer
    return int(squared_digits)


# Uncomment to run and check test cases
print(square_digits(9119))  # Output: 811181
print(square_digits(765))   # Output: 493625
