#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """defines a rectangle
    Args:
        width: width of rectangle
        height: height of rectangle"""

    def __init__(self, width=0, height=0):
        """initialiation of width and height"""
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """to retrieve private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """to set height with new value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must b >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """retrieve private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """to set width with new value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
