# Description

# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

# The output should be two capital letters with a dot separating them.

# It should look like this:

# Sam Harris => S.H

# patrick feeney => P.F


# My Solution
def abbrev_name(name):
    # Split the name into two words using the space as a separator
    words = name.split()

    # Extract the first letter of each word and capitalize them
    first_initial = words[0][0].upper()
    second_initial = words[1][0].upper()

    # Combine the initials with a dot separating them
    initials = first_initial + "." + second_initial

    return initials


# Uncomment to run and check test cases
# print(abbrev_name("Sam Harris"))     # Output: "S.H"
# print(abbrev_name("patrick feeney")) # Output: "P.F"
