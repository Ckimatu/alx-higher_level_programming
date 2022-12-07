#!/usr/bin/python3

# a function that computes the square value
# of all integers of a matrix
# matrix is a 2 dimensional array
# Returns a new matrix

def square_matrix_simple(matrix=[]):
    return ([list(map(lambda x: x * x, i)) for i in matrix])
