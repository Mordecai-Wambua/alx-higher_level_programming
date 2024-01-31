#!/usr/bin/python3
"""
    Function to print txt and applying 2 new lines
    whenever certain symbols are encountered
"""


def text_indentation(text):
    """Function to print text with space formatting on specific symbols
        Args:
            text(string): actual text
    """
    try:
        if type(text) is not str:
            raise TypeError("text must be a string")

        output = ""
        for i in text:
            output += i

            if i in ".?:":
                print(output.strip())
                print()
                output = ""

        if output.strip():
            print(output.strip(), end='')
    except TypeError as ex:
        raise ex
