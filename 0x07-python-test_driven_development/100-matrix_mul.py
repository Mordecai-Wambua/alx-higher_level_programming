#!/usr/bin/python3
"""Function that multiplies 2 matrices."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list): first matrix
        m_b (list): second matrix
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for i in m_a:
        if not isinstance(i, list):
            raise TypeError("m_a must be a list of lists")

    for i in m_b:
        if not isinstance(i, list):
            raise TypeError("m_b must be a list of lists")

    if (m_a == [] or m_a == [[]]):
        raise ValueError("m_a can't be empty")

    if (m_b == [] or m_b == [[]]):
        raise ValueError("m_b can't be empty")

    if not all(type(element) in [int, float]
               for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")

    if not all(type(element) in [int, float]
               for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    output = [[0 for x in range(len(m_b[0]))] for y in range(len(m_a))]
    for row in range(len(m_a)):
        for row2 in range(len(m_b[0])):
            for row3 in range(len(m_b)):
                output[row][row2] += m_a[row][row3] * m_b[row3][row2]

    return (output)
