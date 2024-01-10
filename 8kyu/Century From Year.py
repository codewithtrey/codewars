# Description

# Introduction
# The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

# Task
# Given a year, return the century it is in.

# Examples
# 1705 --> 18
# 1900 --> 19
# 1601 --> 17
# 2000 --> 20


# My Solution
import math

def century(year):
    # Calculate the century by dividing the year by 100 and rounding up
    century = math.ceil(year / 100)
    return century


# Uncomment to run and check test cases
# print(century(1705))  # Output: 18
# print(century(1900))  # Output: 19
# print(century(1601))  # Output: 17
# print(century(2000))  # Output: 20
