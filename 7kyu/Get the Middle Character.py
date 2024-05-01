# Description

# You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

# #Examples:

# Kata.getMiddle("test") should return "es"

# Kata.getMiddle("testing") should return "t"

# Kata.getMiddle("middle") should return "dd"

# Kata.getMiddle("A") should return "A"
# #Input

# A word (string) of length 0 < str < 1000 (In javascript you may get slightly more than 1000 in some test cases due to an error in the test cases). You do not need to test for this. This is only here to tell you that you do not need to worry about your solution timing out.

# #Output

# The middle character(s) of the word represented as a string.


# My Solution
def get_middle(s):
    length = len(s)
    midpoint = length // 2

    if length % 2 == 0:
        # Even length
        return s[midpoint - 1 : midpoint + 1]
    else:
        # Odd length
        return s[midpoint]


# Uncomment to run and check test cases
# print(get_middle("test"))  # Output: "es"
# print(get_middle("testing"))  # Output: "t"
# print(get_middle("middle"))  # Output: "dd"
# print(get_middle("A"))  # Output: "A"
