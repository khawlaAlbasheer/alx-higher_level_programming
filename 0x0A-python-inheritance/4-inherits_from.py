#!/usr/bin/python3
"""check the object is an instance of a class that inherited"""


def inherits_from(obj, a_class):
    """Return True if the object is instance of a class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
