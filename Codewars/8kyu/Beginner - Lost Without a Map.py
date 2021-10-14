"""
Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]
"""

def maps(a):
    result = []
    for x in a:
        result.append(x*2)
    return result
    
#alternative solution
def maps(a):
    return [2 * x for x in a]
    
