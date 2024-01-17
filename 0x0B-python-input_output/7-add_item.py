#!/usr/bin/python3
"""Load, add, save using json"""


import json
from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

py_list = []
filename = 'add_item.json'
try:
    py_list = load_from_json_file(filename)
except Exception:
    save_to_json_file(py_list, filename)
length = len(argv)
if length > 1:
    for i in range(1, length):
        py_list.append(argv[i])
    save_to_json_file(py_list, filename)
