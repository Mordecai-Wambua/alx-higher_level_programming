#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for y in x:
            if y != 0:
                print(" ", end="")
            print("{:d}".format(y), end="")
        print()
