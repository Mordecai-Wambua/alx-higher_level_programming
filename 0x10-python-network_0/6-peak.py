#!/#!/usr/bin/python3
"""Find a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """
    Find the peak in a list of integers
    Args:
        list_of_integers: list
    Return:
        peak: int
    """

    if len(list_of_integers) == 0 or list_of_integers == []:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 2:
        return max(list_of_integers)

    peak = 0
    for i in list_of_integers:
        if peak < i:
            peak = i
    return peak
