# Description

# Can you find the needle in the haystack?

# Write a function findNeedle() that takes an array full of junk but containing one "needle"

# After your function finds the needle it should return a message (as a string) that says:

# "found the needle at position " plus the index it found the needle, so:

# Example(Input --> Output)

# ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5"


# My Solution
def find_needle(haystack):
    # Use the index() method to find the position of "needle" in the list
    index = haystack.index("needle")
    # Return the message with the index
    return f"found the needle at position {index}"


# Uncomment to run and check test case
# print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]))
# Output: "found the needle at position 5"
