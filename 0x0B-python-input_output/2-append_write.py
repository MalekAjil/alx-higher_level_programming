#!/usr/bin/python3
"""
Module Append File
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8) and
    returns the number of characters added

    Args:
        filename: the file name
        text: the text to be written
    """
    if filename is None or filename == "":
        return
    with open(filename, 'a', encoding="UTF8") as fn:
        return fn.write(text)
