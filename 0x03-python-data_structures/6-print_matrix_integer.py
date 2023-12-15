#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    length = len(matrix)
    if length == 1:
        return None
    for row in matrix:
        i = 0
        for e in row:
            i += 1
            if i < len(row):
                print('{:d} '.format(e), end="")
            else:
                print('{:d}'.format(e), end="")
        print()
