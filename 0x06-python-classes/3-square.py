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
        if(type(size) != int):
            raise TypeError("size must be an integer")
        if(size < 0):
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns Area"""
        return (self.__size * self.__size)
