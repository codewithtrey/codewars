# Description

# Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

# None of the arrays will be empty, so you don't have to worry about that!


# My Solution
def remove_every_other(my_list):
    return my_list[::2]


# Uncomment to run and check test case
# print(remove_every_other([1, 2, 3, 4, 5]))  # Output: [1, 3, 5]
