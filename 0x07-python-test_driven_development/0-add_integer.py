#!usr/bin/python3
"""Add Integer"""


def add_integer(a, b=98):
    """ Returns the sum of two integers"""
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
    except TypeError as ex:
        print(ex)
