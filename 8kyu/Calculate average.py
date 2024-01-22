# Description

# Write a function which calculates the average of the numbers in a given list.

# Note: Empty arrays should return 0.


# My Solution
def find_average(numbers):
    if len(numbers) == 0:
        return 0  # Handle the case of an empty list to avoid division by zero

    total = sum(numbers)
    average = total / len(numbers)
    return average


# Uncomment to run and check test cases
# print(find_average([1, 2, 3, 4, 5]))  # Output: 3.0 (average of 1, 2, 3, 4, 5 is 3)
# print(find_average([10, 20, 30]))    # Output: 20.0 (average of 10, 20, 30 is 20)
# print(find_average([]))              # Output: 0 (empty list, average is 0)
