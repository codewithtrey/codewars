# Description

# Nathan loves cycling.

# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

# You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

# For example:

# time = 3 ----> litres = 1

# time = 6.7---> litres = 3

# time = 11.8--> litres = 5


# My Solution
import math

def litres(time):
    return math.floor(time * 0.5)


# Uncomment to run and check test cases
# print(litres(3))     # Expected output: 1
# print(litres(6.7))   # Expected output: 3
# print(litres(11.8))  # Expected output: 5
