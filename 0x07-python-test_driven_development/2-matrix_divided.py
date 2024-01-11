#!/usr/bin/python3
"""matrix_divided divides all elements of a matrix
by div and returns the divided matrix"""


def matrix_divided(matrix, div):
    """ divides all elements of a matrix"""

    typeerror = 'matrix must be a matrix (list of lists) of integers/floats'
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')
    new_mat = []
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        new_list = []
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(typeerror)
            else:
                new_list.append(round(i / div, 2))
        new_mat.append(new_list)
        return new_mat
