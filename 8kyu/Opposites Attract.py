# Description

# Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

# Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.


# My Solution
def lovefunc(flower1, flower2):
    return (flower1 % 2 == 1 and flower2 % 2 == 0) or (
        flower1 % 2 == 0 and flower2 % 2 == 1
    )


# Uncomment to run and check test cases
# print(lovefunc(2, 3))  # Output: True (2 is even, 3 is odd)
# print(lovefunc(4, 6))  # Output: False (Both even)
# print(lovefunc(7, 5))  # Output: False (Both odd)
