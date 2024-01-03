# Description
# You get an array of numbers, return the sum of all of the positives ones.

# Example [1,-4,7,12] => 1 + 7 + 12 = 20

# Note: if there is nothing to sum, the sum is default to 0.


# My Solution
def positive_sum(arr):
    positive_numbers = [num for num in arr if num > 0]

    return sum(positive_numbers)


# Uncomment to run and check test case
# arr = [1, -4, 7, 12]
# print(positive_sum(arr))
