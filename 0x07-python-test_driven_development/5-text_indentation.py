#!/usr/bin/python3
"""Text Identation
"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: .,?,:

    Args:
        text: the text string

    Raises:
        TypeError: if text not a string
    """
    try:
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        for c in range(len(text)):
            if text[c] == '.' or text[c] == '?' or text[c] == ';':
                print(f'{text[c]}\n')
                continue
            else:
                print(text[c], end='')
    except TypeError as te:
        print(te)
