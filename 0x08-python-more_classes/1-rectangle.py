#!usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """defines a rectangle"""
    def __init__(self, width=0, height=0):
        """initialiation of widht and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """to retrieve private instance attribute  width"""
        return self.__width

    @width.setter
    def width(self, value):
        """to set width with new value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must b >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """to set height with new value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
