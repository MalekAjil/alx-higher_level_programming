#!/usr/bin/python3
"""
Module load from JSON file
"""


import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”

    Args:
        filename: the file name
    """
    with open(filename, 'r', encoding="UTF8") as f:
        x = json.load(f)
    return x
