#!/usr/bin/python3
"""
Module BaseGeometry
"""


class BaseGeometry:
    """
    class BaseGeometry
    """
    def area(self):
        """
        returns area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value

        Args:
            name: the string
            value: should be an integer

        Returns:
            True, Flase
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
