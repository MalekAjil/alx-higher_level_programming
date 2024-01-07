#!usr/bin/python3
def matrix_divided(matrix, div):
    """ devides all elements of a matrix """
    try:
        if type(matrix) != list or type(matrix) == float:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if type(div) != int or type(div) != float:
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        res = []
        for r in matrix:
            for l in r:
                res.append(l / r)
         return res
     except (TypeError, ZeroDivisionError) as ex:
         print(ex)

