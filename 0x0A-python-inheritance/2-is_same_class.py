#!/usr/bin/python3
"""
Module is_same_class
"""


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an instance of the specified class

    Args:
        obj: the object
        a_class: the class

    Return:
        True if the object is exactly an instance of the specified class ; otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
