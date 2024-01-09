#!/usr/bin/python3
"""
Module from JSON string
"""


import json


def from_json_string(my_str):
    """
    returns an object (Python data structure) represented by a JSON string

    Args:
        my_str: the string
    """
    return json.JSONDecoder().decode(my_str)
