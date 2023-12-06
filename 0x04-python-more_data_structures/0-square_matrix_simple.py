#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    m = matrix.copy()
    if m is None:
        return None
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] *= m[i][j]
    return m
