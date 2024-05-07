# Description

# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

# Example
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]


# My Solution
def filter_list(l):
    filtered_list = []

    for i in l:
        if type(i) == int:
            filtered_list.append(i)
    return filtered_list


# Uncomment to run and check test cases
print(filter_list([1,2,'a','b']))  # Output: [1,2]
print(filter_list([1,'a','b',0,15]))  # Output: [1,0,15]
print(filter_list([1,2,'aasf','1','123',123]))  # Output: [1,2,123]
