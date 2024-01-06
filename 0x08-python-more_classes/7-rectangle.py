#!/usr/bin/python3
""" Rectangle Class """


class Rectangle:
    """ Represents a rectangle
    area: returns the area of the rectangle
    perimeter: returns perimeter
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __print__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        r = ""
        for h in range(self.__height):
            for w in range(self.__width):
                r += str(self.print_symbol)
            if h != self.__height - 1:
                r += "\n"
        return r

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        r = ""
        for h in range(self.__height):
            for w in range(self.__width):
                r += str(self.print_symbol)
            if h != self.__height - 1:
                r += "\n"
        return r

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __eval__(self):
        return Rectangle(2, 4)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
        del self
