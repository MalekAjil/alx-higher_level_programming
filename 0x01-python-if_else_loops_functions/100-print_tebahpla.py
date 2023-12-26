#!/usr/bin/python3

for d in range(122, 95, -1):
    if d % 2 != 0:
        d -= 32
    print("{:c}".format(d), end='')
