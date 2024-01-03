#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    x = number % 10
else:
    x = number % -10
print("Last digit of {} is {}".format(number, x), end="")
if x > 5:
    print("and is greater than 5")
elif x < 6 and x != 0:
    print("and is less than 6 and not 0")
else:
    print("and is 0")
