#!/usr/bin/python3
"""
Module Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle
    """
    def __init__(self, width, height):
        """
        intializes an object
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        returns the area of rectangle
        """
        return self.__width * self.__height

    def __print__(self):
        """
        prints recangle
        """
        print(f"[Rectangle] {self.__width}/{self.__height}")

    def __str__(self):
        """
        return Rectangle string
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
