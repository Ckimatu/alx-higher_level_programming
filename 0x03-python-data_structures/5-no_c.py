#!/usr/bin/env python3

# a function that removes all characters c and C from a string.

def no_c(my_string):
    newString = my_string.translate({ord(i): None for i in 'cC'})
    return newString
