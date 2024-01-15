#!/usr/bin/python3
"""check the object is an instance of a class that inherited
(directly or indirectly)
from the specified class"""


def inherits_from(obj, a_class):
    """Return True if the object is instance of a class
    or from inherited class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
