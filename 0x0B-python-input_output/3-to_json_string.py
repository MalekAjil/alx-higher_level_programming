#!/usr/bin/python3
"""
Module to JSON string
"""


import json


def to_json_string(my_obj):
    """
    returns the JSON representation of an object (string)

    Args:
        my_obj: JSON object
    """
    return json.dumps(my_obj)
