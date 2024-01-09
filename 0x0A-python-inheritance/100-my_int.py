#!/usr/bin/python3
"""
Module MyInt
"""


class MyInt(int):
    """
    MyInt inherets from int
    """
    def __init__(self, value):
        """
        initialize an object
        """
        if type(value) is int:
            self == value
