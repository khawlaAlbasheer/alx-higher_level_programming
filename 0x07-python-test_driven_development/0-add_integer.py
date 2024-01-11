#!/usr/bin/python3
"""add_integer:
    check the type of givene two value
    return the sum of the integer values"""
def add_integer(a, b=98):

    """add two integers"""

    if type(a) is float or type(b) is float:
        a = int(a)
        b = int(b)
    if type(a) is not int:
        raise TypeError('a must be an integer')
    if type(b) is not int:
        raise TypeError('b must be an integer')
    else:
        return (a + b)
