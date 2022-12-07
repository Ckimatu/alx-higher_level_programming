#!/usr/bin/python3

# a function that adds all unique integers in a list
def uniq_add(my_list=[]):
    output = 0
    for item in set(my_list):
        output += item
    return output
