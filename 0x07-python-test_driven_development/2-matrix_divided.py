#!usr/bin/python3

"""This is the matrix_divided module
It supplies one function, matrix_divided(matrix, div)
that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix and returns a new matrix
    matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception
    Each row of the matrix must be of the same size, otherwise raise a TypeError exception
    div must be a number (integer or float), otherwise raise a TypeError exception
    div can’t be equal to 0, otherwise raise a ZeroDivisionError exception
    All elements of the matrix should be divided by div, rounded to 2 decimal places"""
    if matrix not int and not float:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

