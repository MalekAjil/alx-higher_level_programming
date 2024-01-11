#!/usr/bin/python3
"""Module Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Represents a Rectangle
    Attributes:
        __width: the width of the rectangle
        __height: the height of the rectangle
        __x: the horizontal starting point
        __y: the virtical sstarting point
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """The initializer
        Args:
            width: the width of the rectangle
            height: the height of the rectangle
            x: the horizontal starting point
            y: the virtical sstarting point
            id: the id of the object
        """
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width"""
        if type(value) is int:
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height"""
        if type(value) is int:
            if value > 0:
                self.__height = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """Returns the x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x"""
        if type(value) is int:
            if value >= 0:
                self.__x = value
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """Returns the y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y"""
        if type(value) is int:
            if value >= 0:
                self.__y = value
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

