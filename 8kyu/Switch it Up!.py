# Description

# When provided with a number between 0-9, return it in words.

# Input :: 1

# Output :: "One".

# If your language supports it, try using a switch statement.


# My Solution
def switch_it_up(number):
    num_to_word = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    return num_to_word.get(number, "Invalid number")


# Uncomment to run and check test cases
# print(switch_it_up(1))  # Output: "One"
# print(switch_it_up(5))  # Output: "Five"
# print(switch_it_up(9))  # Output: "Nine"
# print(switch_it_up(10))  # Output: "Invalid number"
