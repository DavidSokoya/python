# I'm new to coding and now I want to get the sum of two arrays... Actually the sum of all their elements. I'll appreciate for your help.

# P.S. Each array includes only integer numbers. Output is a number too.
def array_plus_array(arr1,arr2):
    arr1.extend(arr2)
    res = 0;
    for i in arr1:
        res = res + i
    return res