#!/usr/bin/python3

# function that retrieves an element from a list like in C.
# If idx is negative, the function should return None
# If idx is out of range, return None

def element_at(my_list, idx):
    n = len(my_list)
    if idx < 0:
        return None
    elif idx >= n:
        return None
    else:
        return (my_list[idx])
