#!/usr/bin/python3
"""
Module inherits_from
"""


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of a class  that inherited
    (directly or indirectly) from the specified class ;
    otherwise False

    Args:
        obj: the object
        a_class: the class

    Return:
        returns True if the object is an instance of a class  that inherited
        (directly or indirectly) from the specified class ;
        otherwise False
    """
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
