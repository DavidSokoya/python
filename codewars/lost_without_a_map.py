# Given an array of integers, return a new array with each value doubled.

# For example:

# [1, 2, 3] --> [2, 4, 6]
def maps(a):
    res = []
    
    for num in a:
        res.append(num * 2)
    return res