# Description

# The function is not returning the correct values. Can you figure out why?

# Example (Input --> Output ):

# 3 --> "Earth"

# Original function
# def get_planet_name(id):
#     # This doesn't work; Fix it!
#     name=""
#     switch id:
#         case 1: name = "Mercury"
#         case 2: name = "Venus"
#         case 3: name = "Earth"
#         case 4: name = "Mars"
#         case 5: name = "Jupiter"
#         case 6: name = "Saturn"
#         case 7: name = "Uranus"
#         case 8: name = "Neptune"
#     return name


# My Solution
def get_planet_name(id):
    name = ""
    if id == 1:
        name = "Mercury"
    elif id == 2:
        name = "Venus"
    elif id == 3:
        name = "Earth"
    elif id == 4:
        name = "Mars"
    elif id == 5:
        name = "Jupiter"
    elif id == 6:
        name = "Saturn"
    elif id == 7:
        name = "Uranus"
    elif id == 8:
        name = "Neptune"
    return name


# Uncomment to run and check test case
# print(get_planet_name(3))  # Output: Earth
