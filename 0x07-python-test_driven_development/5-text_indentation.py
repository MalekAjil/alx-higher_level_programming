#!/usr/bin/python3
""""""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text: the text string

    Raises:
        TypeError: if text not a string
    """
    try:
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        for c in text:
            if c == '.' or c == '?' or c == ';':
                print('\n')
            else:
                print(c, end='')
    except TypeError as te:
        print(te)
