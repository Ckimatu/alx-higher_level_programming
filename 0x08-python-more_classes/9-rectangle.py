#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """defines a rectangle:
        Args:
            width: width of rectangle
            height: height of rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialiation of width and height"""
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    def area(self):
        """public instance method that  returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area1 = rect_1.width * rect_1.height
        area2 = rect_2.width * rect_2.height

        return rect_1 if area1 == area2 or area1 > area2 else rect_2

    @classmethod
    def square(cls, size=0):
        """ returns a new Rectangle instance with width == height == size"""
        return (cls(size, size))

    def __str__(self):
        """Returns a printable representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """return representation of the rectangle"""
        if self.width != 0 and self.height != 0:
            return f"Rectangle({self.width}, {self.height})"
        else:
            return ""

    def __del__(self):
        """prints a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
