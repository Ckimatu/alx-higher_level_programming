#!/usr/bin/python3

"""This is the matrix_divided module
It supplies one function, matrix_divided(matrix, div)
"""
    
def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix and returns a new matrix
    matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception
    Each row of the matrix must be of the same size, otherwise raise a TypeError exception
    div must be a number (integer or float), otherwise raise a TypeError exception
    div can’t be equal to 0, otherwise raise a ZeroDivisionError exception
    All elements of the matrix should be divided by div, rounded to 2 decimal places"""

    list_error = "matrix must be a matrix (list of lists) of integers/floats"
    len_error = "Each row of the matrix must have the same size"
    div_int_error = "div must be a number"
    div_zero_error = "division by zero"
    new_matrix = []
    new_list = []
    if not matrix:
        raise TypeError(list_error)
    if type(div) is not int and type(div) is not float:
        raise TypeError(div_int_error)
    if div == 0:
        raise ZeroDivisionError(div_zero_error)
    longitud = len(matrix[0])
    for lista in matrix:
        if type(lista) is not list:
            raise TypeError(list_error)
        if len(lista) != longitud:
            raise TypeError(len_error)
        for item in lista:
            if type(item) is not int and type(item) is not float:
                raise TypeError(list_error)
            num = item / div
            new_list.append(round(num, 2))
        new_matrix.append(new_list)
        new_list = []
    return new_matrix
