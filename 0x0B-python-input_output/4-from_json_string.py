#!/usr/bin/python3
"""return an object reppresented by a JSON str"""


import json


def from_json_string(my_str):
    """take a string
    returns object representation"""
    return json.loads(my_str)
