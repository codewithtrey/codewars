# Description

# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "


# My Solution
def double_char(s):
    result = ""
    for char in s:
        result += char * 2
    return result


# Uncomment to run and check test cases
# print(double_char("String"))      # Output: "SSttrriinngg"
# print(double_char("Hello World")) # Output: "HHeelllloo  WWoorrlldd"
# print(double_char("1234!_ "))     # Output: "11223344!!__  "
