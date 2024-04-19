# Description

# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.


# My Solution
def get_count(sentence):
    vowels = 'aeiou'
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count


# Uncomment to run and check test cases
# print(get_count("hello world"))  # Output: 3
# print(get_count("how are you"))  # Output: 5
# print(get_count("python"))       # Output: 1
