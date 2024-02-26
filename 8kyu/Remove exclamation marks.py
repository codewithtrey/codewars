# Description

# Write function RemoveExclamationMarks which removes all exclamation marks from a given string.


# My Solution
def remove_exclamation_marks(s):
    result = ""
    for char in s:
        if char != "!":
            result += char
    return result


# Uncomment to run and check test cases
# print(remove_exclamation_marks("Hello! World!"))  # Output: "Hello World"
# print(remove_exclamation_marks("This is an example!!"))  # Output: "This is an example"
