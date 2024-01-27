#!/usr/bin/python3
def add_integer(a, b=98):
    """Function that adds two integers
        Args:
            a: first number
            b: second number

        Return:
            the sum of the 2 numbers
    """
    try:
        if type(a) not in [int, float]:
            raise TypeError("a must be an integer")
        elif type(b) not in [int, float]:
            raise TypeError("b must be an integer")

        if type(a) or type(b) is float:
            return(int(a) + int(b))

        return (a + b)
    except Exception as i:
        return (i)
