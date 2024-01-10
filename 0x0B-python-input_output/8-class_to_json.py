#!/usr/bin/python3
"""
Module Calss to JSON
"""


import json


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object

    Args:
        obj: is an instance of a Class

    Returns:
        dictionary description
    """
    return json.dumps(dir(obj))
