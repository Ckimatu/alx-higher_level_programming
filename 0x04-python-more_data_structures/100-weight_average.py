#!/usr/bin/python3

# returns the weighted average of all integers
# tuple (<score>, <weight>)
# Returns 0 if the list is empty

def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        score = 0
        weight = 0
        for a, b in my_list:
            score += (a * b)
            weight += b
    return (score / weight)
