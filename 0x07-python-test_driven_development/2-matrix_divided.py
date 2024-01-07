#!/usr/bin/python3
"""Devide Matrix"""


def matrix_divided(matrix, div):
    """ devides all elements of a matrix """
    try:
        if (not isinstance(matrix, (list, float)) or
                not all(isinstance(row, (list, float)) for row in matrix)):
            raise TypeError("matrix must be a matrix (list of lists)" +
                            " of integers/floats")
        ln = len(matrix[0])
        for row in matrix:
            if len(row) != ln:
                raise TypeError("Each row of the matrix must " +
                                "have the same size")
        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        res = []
        for r in matrix:
            rr = []
            for x in r:
                rr.append(round(x / div, 2))
            res.append(rr)
        return res
    except (TypeError, ZeroDivisionError) as ex:
        print(ex)
