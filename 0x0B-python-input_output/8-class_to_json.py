#!/usr/bin/python3
"""Class to JSON"""


def class_to_json(obj):
    """takes SON serialization of an object
    returns the dictionary description
    with simple data structure"""
    return obj.__dict__
