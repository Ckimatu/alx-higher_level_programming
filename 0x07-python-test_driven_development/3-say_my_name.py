#!/usr/bin/python3

"""A say_my_name module"""

def say_my_name(first_name, last_name=""):
    """ a function that prints My name is <first name> <last name>
    first_name and last_name must be strings otherwise, raise a TypeError exception"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}",)
