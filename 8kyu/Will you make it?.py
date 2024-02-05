# Description

# You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.

# Considering these factors, write a function that tells you if it is possible to get to the pump or not.

# Function should return true if it is possible and false if not.


# My Solution
def zero_fuel(distance_to_pump, mpg, fuel_left):
    # Calculate the maximum distance the car can travel with the remaining fuel
    max_distance = mpg * fuel_left

    # Check if the remaining fuel is enough to reach the pump
    return max_distance >= distance_to_pump


# Uncomment to run and check test cases
# print(zero_fuel(50, 25, 2))   # Output: True (2 gallons * 25 mpg >= 50 miles)
# print(zero_fuel(100, 30, 3))  # Output: False (3 gallons * 30 mpg < 100 miles)
# print(zero_fuel(30, 20, 1))   # Output: False (1 gallon * 20 mpg < 30 miles)
