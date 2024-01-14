#!/usr/bin/python3
"""LockedClass return only first_name"""


class LockedClass:
    """does not prevents the user from dynamically
    creating new instance attributes"""

    __slots__ = ['first_name']
