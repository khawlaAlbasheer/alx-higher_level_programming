#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """writes a string to a text file
    returns the number of characters written"""
    with open(filename, 'w', encoding='utf-8') as f:
        file = f.write(text)
        return file
