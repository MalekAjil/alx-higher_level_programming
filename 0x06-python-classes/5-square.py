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
        if(type(size) != int):
            raise TypeError("size must be an integer")
        elif(size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns Area"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Returns the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size"""
        if(type(value) != int):
            raise TypeError("size must be an integer")
        elif(value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
