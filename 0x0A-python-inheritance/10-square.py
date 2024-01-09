#!/usr/bin/python3
"""
Module Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a Square
    """
    def __init__(self, size):
        """
        intializes an object
        """
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        """
        returns the area of rectangle
        """
        return self.__size * self.__size
