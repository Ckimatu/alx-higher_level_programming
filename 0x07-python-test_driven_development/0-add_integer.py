#!/usr/bin/python3

"""This is the "add_integer" module.
It supplies one function, add_integer(a, b=98)"""


def add_integer(a, b=98):
    """a function that adds 2 integers and returns the result
    a and b must be integers or floats, otherwise raise a TypeError exception
    a and b must be first casted to integers if they are float"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
