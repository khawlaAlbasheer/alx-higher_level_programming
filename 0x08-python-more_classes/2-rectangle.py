#!/usr/bin/python3
"""Rectangle class defines a Rectangle"""


class Rectangle:
    """Rectangle class defines a Rectangle"""

    def __init__(self, width=0, height=0):
        if type(width) is int:
            if width < 0:
                raise ValueError('width must be >= 0')
            self.__width = width
        else:
            raise TypeError('width must be an integer')
        if type(height) is int:
            if height < 0:
                raise ValueError('height must be >= 0')
            self.__height = height
        else:
            raise TypeError('height must be an integer')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
