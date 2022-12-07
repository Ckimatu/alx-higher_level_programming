#!/usr/bin/python3

# returns a new dictionary with all values multiplied by 2
# assume that all values are only integers

def multiply_by_2(a_dictionary):
    new_dictionary = {item: a_dictionary[item] * 2 for item in a_dictionary}
    return (new_dictionary)
