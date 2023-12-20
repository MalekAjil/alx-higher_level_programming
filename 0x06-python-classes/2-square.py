#!/usr/bin/python3
"""Class Square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """The initializer
        Args:
            size (:obj:`int`, optional): the size of the square
        Attributes:
            __size (int): the square size"""
        self.__size = size
        if(type(self.__size) != int):
            raise TypeError("size must be an integer")
        if(self.__size < 0):
            raise ValueError("size must be >= 0")
