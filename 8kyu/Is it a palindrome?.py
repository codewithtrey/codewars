# Description

# Write a function that checks if a given string (case insensitive) is a palindrome.

# A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards, such as madam or racecar.


# My Solution
def is_palindrome(s):
    # Convert the string to lowercase and remove non-alphanumeric characters
    s = "".join(char.lower() for char in s if char.isalnum())
    # Compare the string with its reverse
    return s == s[::-1]


# Uncomment to run and check test cases
# print(is_palindrome("Madam"))  # Output: True
# print(is_palindrome("Racecar"))  # Output: True
# print(is_palindrome("Hello"))  # Output: False
