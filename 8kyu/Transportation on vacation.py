# Description

# After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight for you and your girlfriend and try to leave all the mess behind you.

# You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you some good offers.

# Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total.

# Write a code that gives out the total amount for different days(d).


# My Solution
def rental_car_cost(d):
    total_cost = d * 40  # Calculate the total cost without any discounts

    # Apply discounts based on the number of days rented
    if d >= 7:
        total_cost -= 50
    elif d >= 3:
        total_cost -= 20

    return total_cost


# Uncomment to run and check test cases
# print(rental_car_cost(1))  # Output: 40
# print(rental_car_cost(4))  # Output: 140
# print(rental_car_cost(7))  # Output: 230
