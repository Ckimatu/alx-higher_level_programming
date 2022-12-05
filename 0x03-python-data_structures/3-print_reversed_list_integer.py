#!/usr/bin/python3

#  a function that prints all integers of a list, in reverse order
def print_reversed_list_integer(my_list=[]):
    n = len(my_list)
    if my_list:
        my_list.reverse()
        for i in range(n):
            print("{:d}".format(my_list[i]))
