#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    if matrix[0] is None:
        return None
    new_mat = []
    for row in matrix:
        count = 0
        new_row = []
        for e in row:
            count += 1
            square = e * e
            new_row.append(square)
        new_mat += [new_row]
    return new_mat
