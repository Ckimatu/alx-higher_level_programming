#!/usr/bin/python3

# function that adds 2 tuples.
# Returns a tuple with 2 integers
# 1st element - addition of the first element of each argument
# 2nd element - addition of the second element of each argument
# If tuples < 2, use 0 for each missing integer
# If a tuple > 2 use only the first 2 integers

def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    if len_a < 2:
        if len_a == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0
    if len_b < 2:
        if len_b == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
