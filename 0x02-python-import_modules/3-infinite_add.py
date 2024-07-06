#!/usr/bin/python3
"""Arguments"""
import sys


if __name__ == "__main__":
    sum = 0
    for g in sys.argv[1:]:
        sum += int(g)
    print(sum)
