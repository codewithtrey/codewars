# Description

# Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, and would like to greet him slightly different. She added a special case to her function, but she made a mistake.

# Can you help her?

# def greet(name):
#     return "Hello, {name}!".format(name=name)
#     if name == "Johnny":
#         return "Hello, my love!"


# My Solution
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)


# Uncomment to run and check test cases
print(greet("Alice"))  # Output: "Hello, Alice!"
print(greet("Bob"))  # Output: "Hello, Bob!"
print(greet("Johnny"))  # Output: "Hello, my love!"
