# Description

# In this Kata we are passing a number (n) into a function.

# Your code will determine if the number passed is even (or not).

# The function needs to return either a true or false.

# Numbers may be positive or negative, integers or floats.

# Floats with decimal part non equal to zero are considered UNeven for this kata.


# My Solution
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


# Uncomment to run and check test cases
print(is_even(2))  # Output: True
print(is_even(4))  # Output: True
print(is_even(1))  # Output: False
