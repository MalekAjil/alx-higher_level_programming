#!/usr/bin/python3
"""
Module Read File
"""


def read_file(filename=""):
    """
    reads a text file (UTF8) and prints it to stdout

    Args:
        filename: the file name
    """
    if filename is None or filename == "":
        return
    with open(filename, 'r', encoding="UTF8") as fn:
        print(fn.read())
