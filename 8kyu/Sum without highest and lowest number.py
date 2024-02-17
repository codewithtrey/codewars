# Description

# Task
# Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

# The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

# Mind the input validation.

# Example
# { 6, 2, 1, 8, 10 } => 16
# { 1, 1, 11, 2, 3 } => 6
# Input validation
# If an empty value ( null, None, Nothing etc. ) is given instead of an array, or the given array is an empty list or a list with only 1 element, return 0.


# My Solution
def sum_array(arr):
    # Check for input validation
    if not arr or len(arr) <= 2:
        return 0

    # Remove the highest and lowest elements from the array
    arr_without_extremes = sorted(arr)[1:-1]

    # Sum the remaining elements
    return sum(arr_without_extremes)


# Uncomment to run and check test case
# print(sum_array([6, 2, 1, 8, 10]))  # Output: 16
# print(sum_array([1, 1, 11, 2, 3]))   # Output: 6
