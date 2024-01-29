# Description

# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

# Note: input will never be an empty string


# My Solution
def fake_bin(x):
    result = "".join(["0" if int(digit) < 5 else "1" for digit in x])
    return result


# Uncomment to run and check test cases
# print(fake_bin("01234"))       # Output: "00000" (All digits are below 5)
# print(fake_bin("56789"))       # Output: "11111" (All digits are 5 and above)
