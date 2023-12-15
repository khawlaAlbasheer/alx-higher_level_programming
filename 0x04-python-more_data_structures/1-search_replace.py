#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return None
    if len(my_list) == 0:
        return my_list
    new_list = []
    for elem in my_list:
        if elem == search:
            new_list.append(replace)
        else:
            new_list.append(elem)
    return new_list
