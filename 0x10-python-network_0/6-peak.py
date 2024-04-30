#!/#!/usr/bin/python3
def find_peak(list_of_integers):
    """
    Find the peak in a list of integers
    Args:
        list_of_integers: list
    Return:
        peak: int
    """

    if len(list_of_integers) == 0:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 2:
        return max(list_of_integers)
    
    list_of_integers.sort(reverse=True)
    return list_of_integers[0]
