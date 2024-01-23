# Description

# There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. You want to know if you're better than the average student in your class.

# You receive an array with your peers' test scores. Now calculate the average and compare your score!

# Return True if you're better, else False!


# My Solution
def better_than_average(class_points, your_points):
    if len(class_points) == 0:
        return 0  # Handle the case of an empty list to avoid division by zero

    total = sum(class_points)
    average = total / len(class_points)
    if your_points > average:
        return True
    else:
        return False

# Uncomment to run and check test cases
# print(better_than_average([70, 85, 90, 65, 80], 75))  # Output: False (Your points are not better than the class average)
# print(better_than_average([70, 85, 90, 65, 80], 85))  # Output: True (Your points are better than the class average)
