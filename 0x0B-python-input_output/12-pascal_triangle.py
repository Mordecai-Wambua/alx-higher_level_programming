#!/usr/bin/python3
"""Technical interview question."""


def pascal_triangle(n):
    """Return an integer list representinf Pascal's triangle of n.

    Args:
        n (int): inital value
    """
    if n <= 0:
        return ([])
    pascal = [[1]]
    while len(pascal) != n:
        a = pascal[-1]
        temp = [1]
        for i in range(len(a) - 1):
            temp.append(a[i] + a[i + 1])
        temp.append(1)
        pascal.append(temp)
    return (pascal)
