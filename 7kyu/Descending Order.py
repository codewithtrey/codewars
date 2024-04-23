# Description

# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

# Examples:
# Input: 42145 Output: 54421

# Input: 145263 Output: 654321

# Input: 123456789 Output: 987654321


# My Solution
def descending_order(num):
    # Convert the number to a string, sort the characters in descending order, and join them back into a string
    sorted_digits = "".join(sorted(str(num), reverse=True))
    # Convert the resulting string back to an integer and return it
    return int(sorted_digits)


# Uncomment to run and check test cases
# print(descending_order(123))  # Output: 321
# print(descending_order(42145))  # Output: 54421
# print(descending_order(987654321))  # Output: 987654321
