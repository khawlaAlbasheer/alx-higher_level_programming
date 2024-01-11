#!/usr/bin/python3
"""say_my_name prints a string"""


def say_my_name(first_name, last_name=""):
    """say_my_name checks the type of first_name and last_name
    prints a string of first_name followed by last_name
    no return value"""
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print('My name is {:s} {:s}'.format(first_name, last_name))
