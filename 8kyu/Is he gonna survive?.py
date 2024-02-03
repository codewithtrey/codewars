# Description

# A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a couple of powerful dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?

# Return true if yes, false otherwise :)


# My Solution
def hero(bullets, dragons):
    # Check if the number of bullets is greater than or equal to double the number of dragons
    return bullets >= dragons * 2


# Uncomment to run and check test cases
# print(hero(10, 5))  # Output: True (10 bullets are enough for 5 dragons)
# print(hero(7, 4))   # Output: False (7 bullets are not enough for 4 dragons)
