#!/usr/bin/python3

# function prints a dictionary by ordered keys.
# assume that all keys are strings
# Keys should be sorted by alphabetic order

def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    keys.sort()
    for key in keys:
        print("{}: {}".format(key, a_dictionary[key]))
