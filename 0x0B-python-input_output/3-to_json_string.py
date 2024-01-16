#!/usr/bin/python3
"""usage of json to get str of an obj"""


import json
def to_json_string(my_obj):
    """takes a string object
    returns the JSON representation"""
    return json.dumps(my_obj)
