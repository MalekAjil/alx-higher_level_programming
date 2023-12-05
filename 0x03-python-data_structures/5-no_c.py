#!/usr/bin/python3
def no_c(my_string):
    new = my_string.copy()
    for x in new:
        if x in "cC":
            new.remove(x)
