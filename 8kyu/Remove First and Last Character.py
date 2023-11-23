# DESCRIPTION:
# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry with strings with less than two characters.


# My Solution
def remove_char(s):
    string = s[1:-1]
    return string


# Uncomment to run and check test cases
# s = "string"
# print(remove_char(s))
