#!/usr/bin/python3
def uppercase(str):
    for c in str:
        d = ord(c)
        if d > 96 and d < 123:
            d -= 32
        print("{:c}".format(d), end = '')
    print()
