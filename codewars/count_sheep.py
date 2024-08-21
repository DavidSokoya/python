# If you can't sleep, just count sheep!!

# If you can't sleep, just count sheep!!

# Task:
# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.
def count_sheep(n):
    
    res = ''
    for i in range(n):
       res +=  f"{i+1} sheep..."
    return res