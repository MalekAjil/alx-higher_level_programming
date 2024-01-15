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
