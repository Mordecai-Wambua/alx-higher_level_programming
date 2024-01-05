#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for y in range(0, len(matrix[x])):
            if not y == 0:
                print(" ", end="")
            print("{}".format(matrix[x][y]),end="")
        print()
