#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0
    sm = 0
    wsum = 0
    for row in my_list:
        sm += row[0] * row[1]
        wsum += row[1]
    return sm / wsum
