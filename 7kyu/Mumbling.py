# Description

# This time no story, no theory. The examples below show you how to write function accum:

# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.


# My Solution
def accum(st):
    result = []
    for i, char in enumerate(st):
        result.append(char.upper() + char.lower() * i)
    return "-".join(result)


# Uncomment to run and check test cases
# print(accum("abcd"))     # Output: "A-Bb-Ccc-Dddd"
# print(accum("RqaEzty"))  # Output: "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# print(accum("cwAt"))     # Output: "C-Ww-Aaa-Tttt"
