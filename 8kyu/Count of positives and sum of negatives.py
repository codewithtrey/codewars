# Description

# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].


# My Solution
def count_positives_sum_negatives(arr):
    if not arr:
        return []

    positive_count = sum([1 for x in arr if x > 0])
    negative_sum = sum([x for x in arr if x < 0])

    return [positive_count, negative_sum]


# Uncomment to run and check test case
# print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
# Output: [10, -65]
