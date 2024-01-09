#!/usr/bin/python3
"""
Module save to JSON file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation

    Args:
        my_obj: JSON object
        filename: the file name
    """
    with open(filename, 'w', encoding="UTF8") as f:
        json.dump(my_str, f)
