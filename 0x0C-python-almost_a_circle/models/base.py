#!/usr/bin/python3
"""Module Base class
"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """the Initialzer
        Args:
            id: the object id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
