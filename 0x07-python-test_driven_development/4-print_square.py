#!/usr/bin/python3
"""
Print Square module
"""


def print_square(size):
    """ prints a square

    Args:
        size: the size legth of the square

    Raises:
        TypeError if size is not an integer
    """
    try:

        if type(size) is not int or (type(size) is float and size < 0):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        for i in range(size):
            for j in range(size):
                print("#", end='')
            print()
    except (TypeError, ValueError) as tv:
        print(tv)
