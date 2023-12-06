#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = list(map(lambda x: x**2, range(len(matrix))))
    return squares
