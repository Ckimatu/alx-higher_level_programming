#!/usr/bin/python3

# function replaces an element of a list at a specific position
# if idx is -ve, function should return the original list
# If idx is out of range, the function should return the original list

def replace_in_list(my_list, idx, element):
    n = len(my_list)
    if idx < 0:
        return my_list
    elif idx >= n:
        return my_list
    else:
        my_list[idx] = element
        return my_list
