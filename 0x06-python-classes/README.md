Task 00:(0-square.py)
empty class Square that defines a square

Task 01:(1-square.py)
Private instance attribute: size
Instantiation with size (no type/value verification)

Task 02:(2-square.py)
Instantiation with optional size: def __init__(self, size=0):
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0

Task 03:(3-square.py)
Public instance method: def area(self): that returns the current square area

Task 04:(4-square.py)
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0

Task 05:(5-square.py)
Public instance method: def my_print(self): that prints in stdout the square with the character #:
if size is equal to 0, print an empty line

Task 06:(6-square.py)
Private instance attribute: position:
property def position(self): to retrieve it
property setter def position(self, value): to set it:
position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers
Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0))
position should be use by using space - Don’t fill lines by spaces when position[1] > 0
