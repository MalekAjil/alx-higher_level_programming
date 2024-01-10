#!/usr/bin/python3
"""
This is the "0-add_integer" module.

The 0-add_integer module supplies one function, add_integer().  For example,

>>> add_integer(1, 2)
3
"""


def add_integer(a, b=98):
    """Adds two integers and returns the result.

    Args:
        a: first integer for addition
        b: second integer for addition (optional, default is 98)

    Returns:
        sum of two integers

    Raises:
        TypeError: if a or b are not integers or floats
    """
    try:
        if (type(a) != float and type(a) != int):
            raise TypeError("a must be an integer")
        if (type(b) != int and type(b) != float):
            raise TypeError("b must be an integer")
        if type(a) == float:
            a = int(a)
            if type(b) == float:
                b = int(b)
        return a + b
    except TypeError as te:
        print(te)
