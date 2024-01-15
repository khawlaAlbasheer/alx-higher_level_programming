#!/usr/bin/python3
"""BaseGeometry is an empty class"""


class BaseGeometry:
    """empty class"""
    def area(self):
        """raise Exception error"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """"""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
