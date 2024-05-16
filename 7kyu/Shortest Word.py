# Description

# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.


# My Solution
def find_short(s):
    # Split the string into words
    words = s.split()
    # Find the length of each word
    word_lengths = [len(word) for word in words]
    # Return the minimum length
    return min(word_lengths)


# Uncomment to run and check test cases
# print(find_short("Hello world"))  # Output: 5
# print(find_short("This is a test"))  # Output: 1
