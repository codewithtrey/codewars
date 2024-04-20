# Description

# Trolls are attacking your comment section!

# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

# Your task is to write a function that takes a string and return a new string with all vowels removed.

# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

# Note: for this kata y isn't considered a vowel.


# My Solution
def disemvowel(string_):
    vowels = "aeiouAEIOU"
    result = ""
    for char in string_:
        if char not in vowels:
            result += char
    return result


# Uncomment to run and check test cases
# print(disemvowel("This website is for losers LOL!"))  # Output: "Ths wbst s fr lsrs LL!"
# print(disemvowel("Hello World"))                      # Output: "Hll Wrld"
# print(disemvowel("Python is awesome"))                # Output: "Pythn s wsm"
