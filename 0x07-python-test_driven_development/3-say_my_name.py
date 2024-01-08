#!usr/bin/python3
"""Say my name module"""

def say_my_name(first_name, last_name=""):
    """prints My name is <first name> <last name>

    Args:
        first_name: the first name
        last_name: the last name default ""

    Raises:
        TypeError: if first_name or last_name are not strings
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
