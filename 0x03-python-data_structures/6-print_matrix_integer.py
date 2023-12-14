#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    length = len(matrix)
    if length == 1:
        return None
    for i in range(length):
        for j in range(length):
            if j == length - 1:
                print('{:d}'.format(matrix[i][j]), end="")
            else:
                print('{:d} '.format(matrix[i][j]), end="")
        print()
