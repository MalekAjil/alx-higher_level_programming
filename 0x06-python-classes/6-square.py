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

    def __init__(self, size=0, position=(0, 0)):
        """The initializer
        Args:
            size (:obj:`int`, optional): the size of the square
            position (:obj:`int`, optional): the size of the square
        Attributes:
            __size (int): the square size
            __position (int): the square position"""
        if(type(size) != int):
            raise TypeError("size must be an integer")
        elif(size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
        if type(position) != tuple or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        """Returns the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position"""
        if type(value) != tuple or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1])
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
