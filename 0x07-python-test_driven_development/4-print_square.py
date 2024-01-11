#!/usr/bin/python3
"""print_square print square with the # width size
check the type of size to be positive integer
if size is float raise type error
of size is negative raise value error"""


def print_square(size):
    """prints a square with the character #"""

    if type(size) is not int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    elif type(size) is float or size < 0:
        raise TypeError('size must be integer')
    else:
        for i in range(size):
            for j in range(size):
                print('#', end="")
            print()
