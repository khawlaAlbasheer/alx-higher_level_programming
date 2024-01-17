#!/usr/bin/python3
"""define class Student that retrieves
dictionary representation of it's abjects"""


class Student:
    """class Student that defines a student by:
    Public instance attributes:
    first_name, last_name, age"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        if attrs is not None:
            res = {k: self.__dict__[k] for k in self.__dict__.keys() & attrs}
            return res
        return self.__dict__
