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
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size"""
        if type(value) is int:
            if value > 0:
                self.width = value
                self.height = value
            else:
                raise ValueError("size must be > 0")
        else:
            raise TypeError("size must be an integer")

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        Args:
            args: the arguments
            kwargs: key-worded argument
        """
        if len(args) == 0 and kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            if len(args) >= 1 and args[0] is not None:
                self.id = args[0]
            if len(args) >= 2 and args[1] is not None:
                self.size = args[1]
            if len(args) >= 3 and args[2] is not None:
                self.x = args[2]
            if len(args) == 4 and args[3] is not None:
                self.y = args[3]
