# Description

# Clock shows h hours, m minutes and s seconds after midnight.

# Your task is to write a function which returns the time since midnight in milliseconds.

# Example:
# h = 0
# m = 1
# s = 1

# result = 61000


# My Solution
def past(h, m, s):
    # Convert hours, minutes, and seconds to milliseconds
    milliseconds = (h * 3600 + m * 60 + s) * 1000
    return milliseconds


# Uncomment to run and check test case
# print(past(0, 1, 1))  # Output: 61000 (1 minute and 1 second converted to milliseconds)
