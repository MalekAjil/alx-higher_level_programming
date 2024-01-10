#!/usr/bin/python3
"""Text Indentation
"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: .,?,:

    Args:
        text: the text string

    Raises:
        TypeError: if text not a string
    """
    try:
        cc = ''
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        for c in text:
            print(c, end='')
            if c in ".?:":
                print('\n')
    except TypeError as te:
        print(te)
