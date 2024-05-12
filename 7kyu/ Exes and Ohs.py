# Description

# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

# Examples input/output:

# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false


# My Solution
def xo(s):
    # Convert the string to lowercase to make it case insensitive
    s = s.lower()
    # Count the occurrences of 'x' and 'o'
    count_x = s.count("x")
    count_o = s.count("o")
    # Return True if the counts are equal, False otherwise
    return count_x == count_o


# Uncomment to run and check test cases
# print(xo("ooxx"))   # Output: True
# print(xo("xooxx"))  # Output: False
# print(xo("ooxXm"))  # Output: True
# print(xo("zpzpzpp"))# Output: True
# print(xo("zzoo"))   # Output: False
