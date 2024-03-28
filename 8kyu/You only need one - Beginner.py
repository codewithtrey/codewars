# Description

# You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

# Array can contain numbers or strings. X can be either.

# Return true if the array contains the value, false if not.


# My Solution
def check(seq, elem):
    if elem in seq:
        return True
    else:
        return False


# Uncomment to run and check test cases
# print(check([1,2,3], 1))  # Output: True
# print(check([1,2,3], 4))  # Output: False
