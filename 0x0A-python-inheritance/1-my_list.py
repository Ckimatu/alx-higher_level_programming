#!/usr/bin/python3
"""Inheritance module"""


class MyList(list):
    """Inherits from list and prints sorted list(ascending)"""

    def print_sorted(self):
        """sorts the list in ascending order"""
        print(sorted(self))
