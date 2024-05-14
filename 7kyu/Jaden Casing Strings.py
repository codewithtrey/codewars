# Description

# Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.

# Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

# Example:

# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
# Link to Jaden's former Twitter account @officialjaden via archive.org


# My Solution
def to_jaden_case(string):
    # Split the string into words
    words = string.split()
    # Capitalize the first letter of each word
    jaden_case_words = [word.capitalize() for word in words]
    # Join the words back together into a single string
    jaden_case_string = " ".join(jaden_case_words)
    return jaden_case_string


# Uncomment to run and check test case
# quote = "How can mirrors be real if our eyes aren't real"
# print(to_jaden_case(quote))
