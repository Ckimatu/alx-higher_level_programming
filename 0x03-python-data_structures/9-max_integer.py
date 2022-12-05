#!/usr/bin/python3

# a function that finds the biggest integer of a list.
# If the list is empty, return None

def max_integer(my_list=[]):
    n = len(my_list)
    if n == 0:
        return None

    result = my_list[0]
    for i in range(n):
        if my_list[i] > result:
            result = my_list[i]
    return result
