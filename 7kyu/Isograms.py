# Description

# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# Example: (Input --> Output)

# "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

# isIsogram "Dermatoglyphics" = true
# isIsogram "moose" = false
# isIsogram "aba" = false


# My Solution
def is_isogram(string):
    # Convert the string to lowercase and create a set of its characters
    lower_string = string.lower()
    char_set = set(lower_string)
    # Check if the length of the set is equal to the length of the string
    return len(char_set) == len(lower_string)


# Uncomment to run and check test cases
# print(is_isogram("Dermatoglyphics"))  # Output: True
# print(is_isogram("aba"))  # Output: False
# print(is_isogram("moOse"))  # Output: False
