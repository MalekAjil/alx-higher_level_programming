#!/usr/bin/python3
"""
Module Write File
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8) and
    returns the number of characters written

    Args:
        filename: the file name
        text: the text to be written
    """
    if filename is None or filename == "":
        return
    with open(filename, 'w', encoding="UTF8") as fn:
        return fn.write(text)
