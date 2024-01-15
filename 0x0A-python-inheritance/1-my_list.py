#!/usr/bin/python3
"""Mylist class inherits from list
prints sorted list"""


class MyList(list):
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
