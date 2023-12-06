#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = matrix.copy()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            squares[i][j] = matrix[i][j] ** 2
    return squares
