# Description

# You're writing code to control your town's traffic lights. You need a function to handle each change from green, to yellow, to red, and then to green again.

# Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to.

# For example, when the input is green, output should be yellow.


# My Solution
def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"


# Uncomment to run and check test cases
# print(update_light("green"))  # Output: "yellow"
# print(update_light("yellow")) # Output: "red"
# print(update_light("red"))    # Output: "green"
