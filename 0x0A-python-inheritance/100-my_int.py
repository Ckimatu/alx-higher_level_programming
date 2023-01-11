#!/usr/bin/python3

"""this module inverts comparison operators"""

class MyInt(int):
    """creates a personalised int"""

    def __init__(self, num):
        """initializes the class"""
        self.num = num

    def __eq__(self, other):
        """handles the == operator"""
        return self.num.__ne__(other)

    def __ne__(self, other):
        """reverts the != operator"""
        return self.num.__eq__(other)
