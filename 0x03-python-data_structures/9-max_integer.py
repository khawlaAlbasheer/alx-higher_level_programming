#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    max_elem = my_list[0]
    for elem in my_list:
        if max_elem < elem:
            max_elem = elem
    return max_elem
