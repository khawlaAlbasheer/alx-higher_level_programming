#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        a_dictionary.pop(key)
    new_dict = a_dictionary.copy()
    return new_dict
