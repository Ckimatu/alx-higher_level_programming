#!/usr/bin/env python3

# a function that removes all characters c and C from a string.

def no_c(my_string):
    newString = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            newString += i
    return newString
