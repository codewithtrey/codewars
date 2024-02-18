# Description

# It's the academic year's end, fateful moment of your school report. The averages must be calculated. All the students come to you and entreat you to calculate their average for them. Easy ! You just need to write a script.

# Return the average of the given array rounded down to its nearest integer.

# The array will never be empty.


# My Solution
def get_average(marks):
    total_marks = sum(marks)
    average = total_marks / len(marks)
    return int(average)


# Uncomment to run and check test cases
# print(get_average([70, 80, 90]))  # Output: 80
# print(get_average([85, 90, 92, 88]))  # Output: 88
