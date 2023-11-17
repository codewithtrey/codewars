# DESCRIPTION:
# Complete the square sum function so that it squares each number passed into it and then sums the results together.


# My Solution
def square_sum(numbers):
    sum = 0
    for num in numbers:
        num = num**2
        sum += num
    return sum


# Uncomment to run and check test cases
# numbers = [1,2,2]
# print(square_sum(numbers))
