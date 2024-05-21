# Description

# Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

# Your task is to write a function maskify, which changes all but the last four characters into '#'.

# Examples (input --> output):
# "4556364607935616" --> "############5616"
#      "64607935616" -->      "#######5616"
#                "1" -->                "1"
#                 "" -->                 ""

# // "What was the name of your first pet?"
# "Skippy" --> "##ippy"
# "Nananananananananananananananana Batman!" --> "####################################man!"


# My Solution
def maskify(cc):
    # If the input string is less than or equal to 4 characters, return it as is
    if len(cc) <= 4:
        return cc

    # Otherwise, mask all but the last four characters
    masked = "#" * (len(cc) - 4) + cc[-4:]
    return masked


# Uncomment to run and check test cases
# print(maskify("4556364607935616"))          # Output: "############5616"
# print(maskify("64607935616"))               # Output: "#######5616"
# print(maskify("1"))                         # Output: "1"
# print(maskify(""))                          # Output: ""
