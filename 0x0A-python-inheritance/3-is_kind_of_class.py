#!/usr/bin/python3
"""check the gevin obj is instance of a class
or isnatnce of class that inherited from"""


def is_kind_of_class(obj, a_class):
    """return True if the abject is instance of a class"""
    if isinstance(obj, a_class):
        return True
    return False
