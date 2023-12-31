# Description

# Summation
# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

# For example (Input -> Output):

# 2 -> 3 (1 + 2)
# 8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)


# My Solution
def summation(num):
    if num <= 0:
        return 0
    else:
        total = 0
        for i in range(1, num + 1):
            total += i
        return total


# Uncomment to run and check test case
# num = 6
# print(summation(num))
