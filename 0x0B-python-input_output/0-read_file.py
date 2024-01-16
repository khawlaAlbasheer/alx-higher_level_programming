#!/usr/bin/python3
"""function to read a text file"""


def read_file(filename=""):
    """function that reads a text file
    and prints it to stdout"""
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')
