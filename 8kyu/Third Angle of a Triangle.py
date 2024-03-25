# Description

# You are given two interior angles (in degrees) of a triangle.

# Write a function to return the 3rd.

# Note: only positive integers will be tested.

# https://en.wikipedia.org/wiki/Triangle


# My Solution
def other_angle(a, b):
    return 180 - a - b


# Uncomment to run and check test case
# print(other_angle(45, 45))  # Output: 90
# print(other_angle(30, 60))  # Output: 90
