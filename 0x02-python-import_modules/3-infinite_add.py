#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = 0
    for y in sys.argv:
        if y != sys.argv[0]:
            x += int(y)
    print(x)
