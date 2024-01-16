#!/usr/bin/python3
"""Module Base class
"""
import json


class Base:
    """This class will be the “base” of all other classes
    in this project. The goal of it is to manage id attribute
    in all your future classes and to avoid duplicating the same code
    """
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

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        Args:
            cls: the class name
            list_objs: is a list of instances who inherits of Base
        """
        if list_objs is None:
            list_objs = []
        json_list = cls.to_json_string([o.to_dictionary() for o in list_objs])
        fn = cls.__name__ + ".json"
        with open(fn, "w") as fp:
            fp.write(json_list)

    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string
        Args:
            json_string: is a string representing a list of dictionaries
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        Args:
            cls: the class name
            dictionary: can be thought of as a double pointer to a dictionary
        """
        tmp = cls(1, 1)
        tmp.update(**dictionary)
        return tmp

    def load_from_file(cls):
        """returns a list of instances
        Args:
            cls: the class name
        """
        pass
