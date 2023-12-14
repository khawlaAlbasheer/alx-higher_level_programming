#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        return None
    length = len(my_list)
    if length == 0:
        return None
    length -= 1
    while length >= 0:
        print('{:d}'.format(my_list[length]))
        length -= 1
