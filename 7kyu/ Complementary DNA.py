# Description

# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

# If you want to know more: http://en.wikipedia.org/wiki/DNA

# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

# More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

# Example: (input --> output)

# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"


# My Solution
def DNA_strand(dna):
    # Create a dictionary mapping each base to its complement
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}

    # Use a list comprehension to generate the complementary strand
    complementary_strand = "".join([complement[base] for base in dna])

    return complementary_strand


# Uncomment to run and check test cases
# print(DNA_strand("ATTGC"))  # Output: "TAACG"
# print(DNA_strand("GTAT"))  # Output: "CATA"
