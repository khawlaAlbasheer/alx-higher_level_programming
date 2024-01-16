#!/usr/bin/python3
import json
"""usage of json to get str of an obj"""


def to_json_string(my_obj):
    """takes a string object
    returns the JSON representation"""
    return json.dumps(my_obj)
