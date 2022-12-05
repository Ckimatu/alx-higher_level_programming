#!/usr/bin/python3

#  a function that replaces an element in a list at a specific position
# without modifying the original list (like in C)
# If idx is negative, return a copy of the original list
# If idx is out of range, return a copy of the original list

def new_in_list(my_list, idx, element):
    n = len(my_list)
    newList = my_list.copy()
    if idx < 0:
        return my_list.copy()
    elif idx >= n:
        return my_list.copy()
    else:
        newList[idx] = element
        return newList
