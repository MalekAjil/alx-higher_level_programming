#!/usr/bin/python3
"""Arguments"""
import sys


if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)
    if argc == 1:
        print("0 arguments.")
    elif argc == 2:
        print("1 argument:\n1: {0}".format(argv[1]))
    else:
        print("{0} arguments:".format(argc - 1))
        n = 1
        for g in argv[1:]:
            print("{0}: {1}".format(n, argv[n]))
            n += 1
