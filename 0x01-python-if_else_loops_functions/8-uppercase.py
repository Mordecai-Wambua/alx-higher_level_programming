#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            x = 32
        else:
            x = 0
        print("{:c}".format(ord(i) - x), end="")
    print("")
