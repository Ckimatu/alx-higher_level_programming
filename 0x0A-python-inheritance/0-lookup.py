#!/usr/bin/python3
"""Inheritance module"""


def lookup(obj):
    """This function returns a list of all available attributes  and methods of an object"""
    avail = dir(obj)
    return list(avail)
