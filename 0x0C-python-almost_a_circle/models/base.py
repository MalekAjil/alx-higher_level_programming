#!/usr/bin/python3
"""Module Base class
"""
import json
import os
import csv


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string
        Args:
            json_string: is a string representing a list of dictionaries
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        Args:
            cls: the class name
            dictionary: can be thought of as a double pointer to a dictionary
        """
        tmp = cls(1, 1)
        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        """returns a list of instances
        Args:
            cls: the class name
        """
        fn = cls.__name__ + ".json"
        if not os.path.exists(fn):
            return []
        with open(fn, "r") as fp:
            str = fp.read()
        list_dicts = cls.from_json_string(str)
        list_instances = [cls.create(**d) for d in list_dicts]
        return list_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialises in CSV
        Args:
            cls: the class
            list_objs: list of objects
        """
        fn = cls.__name__+".csv"
        if list_objs is None:
            list_objs = []
        with open(fn, "w", newline="") as f:
            writer = csv.writer(f)
            for obj in list_objs:
                dict_obj = obj.to_dictionary()
                if cls.__name__ == "Rectangle":
                    list_obj = [dict_obj["id"], dict_obj["width"],
                            dict_obj["height"], dict_obj["x"], dict_obj["y"]]
                elif cls.__name__ == "Square":
                    list_obj = [dict_obj["id"], dict_obj["size"],
                            dict_obj["x"], dict_obj["y"]]
                writer.writerow(list_obj)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes in CSV"""
        fn = cls.__name__+".csv"
        list_instances = []
        with open(fn, "r", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    dict_obj = {"id": int(row[0]), "width": int(row[1]),
                            "height": int(row[2]), "x": int(row[3]), "y": int(row[4])}
                elif cls.__name__ == "Square":
                    dict_obj = {"id": int(row[0]), "size": int(row[1]),
                            "x": int(row[2]), "y": int(row[3])}
                instance = cls.create(**dict_obj)
                list_instances.append(instance)
        return list_instances
