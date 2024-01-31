#!/usr/bin/python3
"""Function that divides matrix elements by the argument div."""


def matrix_divided(matrix, div):
    """Divides all matrix elements by div.

    Args:
        matrix (list): The actual matrix
        div (int/float): divisor

    Returns:
        the new matrix after division

    """
    try:
        msg = "missing the required positional arguments: 'matrix' and 'div'"
        msg2 = "matrix must be a matrix (list of lists) of integers/floats"
        if (matrix is None or div is None):
            raise TypeError(msg)

        if type(div) not in [int, float]:
            raise TypeError("div must be a number")

        if div == 0:
            raise ZeroDivisionError("division by zero")

        if (not isinstance(matrix, list) or
                matrix == [] or
                not all(isinstance(row, list) for row in matrix) or
                not all((isinstance(i, (int, float))
                        for row in matrix for i in row))):
            raise TypeError(msg2)

        if not all(len(row) == len(matrix[0]) for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")

        return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]

    except (TypeError, ZeroDivisionError) as i:
        raise (i)
