#!/usr/bin/python3

"""Define a magic class matching a bytecode provided by Alx."""

import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a magic class.
        Arg:
            radius (float or int): The radius of the new magic class.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the magic class."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The circumference of the magic class."""
        return (2 * math.pi * self.__radius)
