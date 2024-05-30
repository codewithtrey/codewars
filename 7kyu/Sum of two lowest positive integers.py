# Description

# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

# For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

# [10, 343445353, 3453445, 3453545353453] should return 3453455.


# My Solution
def sum_two_smallest_numbers(numbers):
    # Step 1: Sort the array in ascending order
    sorted_numbers = sorted(numbers)

    # Step 2: Sum the first two elements
    return sorted_numbers[0] + sorted_numbers[1]


# Uncomment to run and check test cases
# print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))  # Output: 7
# print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453]))  # Output: 3453455
# print(sum_two_smallest_numbers([15, 22, 3, 9, 18, 27]))  # Output: 12
# print(sum_two_smallest_numbers([6, 8, 12, 3, 4]))  # Output: 7
