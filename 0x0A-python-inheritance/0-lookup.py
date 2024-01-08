#!/usr/bin/python3
"""
lookup module
"""


def lookup(obj):
    """
    returns the list of available attributes and methods of an object

    Args:
        obj: object
    """
    return obj.__dict___
