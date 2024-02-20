# Description

# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

# Return your answer as a number.


# My Solution
def sum_mix(arr):
    return sum(map(int, arr))


# Uncomment to run and check test cases
# print(sum_mix([9, 3, '7', '3']))  # Output: 22 (9 + 3 + 7 + 3)
# print(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]))  # Output: 42 (5 + 0 + 9 + 3 + 2 + 1 + 9 + 6 + 7)
