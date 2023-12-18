#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    v = 0
    while i < x:
        try:
            print('{:d}'.format(my_list[i]), end="")
            v += 1
            i += 1
        except (TypeError, ValueError):
            i += 1
    print()
    return v
