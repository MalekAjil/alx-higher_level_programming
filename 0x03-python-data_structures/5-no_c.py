#!/usr/bin/python3
def no_c(my_string):
    new = my_string
    for x in  range(len(my_string)):
        if my_string[x] not in "cC":
            new.append(x)
    return (new)
