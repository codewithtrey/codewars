# Description

# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

# invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
# invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
# invert([]) == []
# You can assume that all values are integers. Do not mutate the input array/list.


# My Solution
def invert(lst):
    inverted_list = [-x for x in lst]
    return inverted_list

# Uncomment to run and check test cases
# print(invert([1, 2, 3, 4, 5]))     # Output: [-1, -2, -3, -4, -5]
# print(invert([1, -2, 3, -4, 5]))  # Output: [-1, 2, -3, 4, -5]
# print(invert([]))                 # Output: [] (Empty list remains empty)
