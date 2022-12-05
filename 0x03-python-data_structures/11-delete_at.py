#!/usr/bin/python3

# a function that deletes the item at a specific position in a list
# uf idx is -ve or out of range, returns the same list

def delete_at(my_list=[], idx=0):
    for i in range(len(my_list)):
        if idx < 0 or idx >= len(my_list):
            return my_list
        else:
            del my_list[idx]
            return my_list
