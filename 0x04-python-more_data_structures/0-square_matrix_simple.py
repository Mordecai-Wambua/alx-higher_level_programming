#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    z = list(map(lambda row: [x**2 for x in row], matrix))
    return z
