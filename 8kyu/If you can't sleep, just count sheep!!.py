# Description

# Task:
# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.


# My Solution
def count_sheep(n):
    murmur = ""
    for i in range(1, n + 1):
        murmur += str(i) + " sheep..."
    return murmur


# Uncomment to run and check test case
print(count_sheep(3))  # Output: "1 sheep...2 sheep...3 sheep..."
