#!/usr/bin/python3
"""Devide Matrix"""


def matrix_divided(matrix, div):
    """divide matrix by div and returns the result.

    Args:
        matrix: list of lists of integers or floats
        div: the division

    Returns:
        matrix devided by div

    Raises:
        TypeError: if matrix elements not integers or floats
        """
    try:
        if not isinstance(matrix, (list, float)):
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        for row in matrix:
            for x in row:
                if not isinstance(x, (list, int, float)):
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
        return ex
