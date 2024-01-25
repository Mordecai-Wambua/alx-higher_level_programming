#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        output = fct(*args)
        return (output)
    except Exception as i:
        sys.stderr.write("Exception: {}\n".format(i))
        return None
