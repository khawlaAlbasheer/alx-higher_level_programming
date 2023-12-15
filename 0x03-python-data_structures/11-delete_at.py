#!/usr/bin/python
def delete_at(my_list=[], idx=0):
    if my_list is None:
        return None
    length = len(my_list)
    if length == 0:
        return None
    if idx < 0 or idx >= length:
        return my_list
    new_list = []
    for i in range(length):
        if i != idx:
            new_list.append(my_list[i])
        else:
            continue
    my_list[:] = new_list[:]
    return my_list
