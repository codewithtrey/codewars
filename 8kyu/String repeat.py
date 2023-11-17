# Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.

# Examples (input -> output)
# 6, "I"     -> "IIIIII"
# 5, "Hello" -> "HelloHelloHelloHelloHello"


# My Solution
def repeat_str(repeat, string):
    return string * repeat


# Uncomment to run and check test cases
# repeat = 6
# string = "I"
# print(repeat_str(repeat, string))

# repeat = 5
# string = "Hello"
# print(repeat_str(repeat, string))
