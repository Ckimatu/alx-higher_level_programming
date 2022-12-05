#!/usr/bin/python3

# a function that finds all multiples of 2 in a list.
# Return a new list with True or False

def divisible_by_2(my_list=[]):
    is_even = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            is_even.append(True)
        else:
            is_even.append(False)

    return is_even
