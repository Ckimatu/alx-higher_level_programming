#!/usr/bin/python3

""" prints a square with the character #"""


def print_square(size):
    """size is the size length of the square
    size must be an integer, otherwise raise a TypeError
    if size is less than 0, raise a ValueError
    f size is a float and is less than 0, raise a TypeError
    tests:
        >>> print_square(1)
        #
        >>> print_square(2)
        ##
        ##
        >>> print_square(0)


        """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(1, size + 1):
            for j in range(size):
                print("#", end="")
            print()
