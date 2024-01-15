#!/usr/bin/python3
"""Square Module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """The initializer
        Args:
            size: the size of the square
            x: the horizontal position
            y: the vertical position
            id: the object id
        """
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Returns the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size"""
        if type(value) is int:
            if value > 0:
                self.__size = value
            else:
                raise ValueError("size must be > 0")
        else:
            raise TypeError("size must be an integer")

