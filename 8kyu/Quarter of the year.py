# Description

# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

# For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.


# My Solution
def quarter_of(month):
    if month <= 3:
        return 1
    elif month <= 6:
        return 2
    elif month <= 9:
        return 3
    else:
        return 4


# Uncomment to run and check test cases
# print(quarter_of(2))   # Output: 1
# print(quarter_of(6))   # Output: 2
# print(quarter_of(11))  # Output: 4
