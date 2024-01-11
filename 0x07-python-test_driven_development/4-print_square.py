#!/usr/bin/python3
def print_square(size):
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
