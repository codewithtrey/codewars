# Description

# Given an array of integers, return a new array with each value doubled.

# For example:

# [1, 2, 3] --> [2, 4, 6]


# My Solution
def maps(a):
    # Use a list comprehension to create a new list with each value doubled
    doubled_values = [x * 2 for x in a]
    return doubled_values


# Uncomment to run and check test case
# print(maps([1, 2, 3]))  # Output: [2, 4, 6]
