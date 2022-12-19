#!/usr/bin/python3

# safe_print_integer - prints an integer with "{:d}".format().
# Args: value (int): The integer to print
# Return: If a TypeError or ValueError occurs - False.
# Otherwise - True.

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
