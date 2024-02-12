# Description

# Write a function to split a string and convert it into an array of words.

# Examples (Input ==> Output):
# "Robin Singh" ==> ["Robin", "Singh"]

# "I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]


# My Solution
def string_to_array(s):
    if not s:  # Check if the input string is empty
        return [""]
    return s.split()


# Uncomment to run and check test cases
# print(string_to_array(""))  # Output: [""]
# print(string_to_array("Robin Singh"))  # Output: ["Robin", "Singh"]
# print(string_to_array("I love arrays they are my favorite"))  # Output: ["I", "love", "arrays", "they", "are", "my", "favorite"]
