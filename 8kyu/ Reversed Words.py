# Description

# Complete the solution so that it reverses all of the words within the string passed in.

# Words are separated by exactly one space and there are no leading or trailing spaces.

# Example(Input --> Output):

# "The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"


# My Solution
def reverse_words(s):
    # Split the string into words, reverse the list of words, and join them back into a string
    return " ".join(reversed(s.split()))


# Uncomment to run and check test case
print(reverse_words("The greatest victory is that which requires no battle"))
# Output: "battle no requires which that is victory greatest The"
